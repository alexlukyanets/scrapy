import scrapy
import json
from scrapy.loader import ItemLoader
from permits.items import PermitItem
from scrapy.loader.processors import TakeFirst


def gen_contact(n):
    n += 1
    name = f'contact_{n}_name,'
    city = f'contact_{n}_city,'
    state = f'contact_{n}_state,'
    zipcode = f'contact_{n}_zipcode,'
    return name + city + state + zipcode


def parse_contact(permit):
    to_contact = []

    for contact in PermitSpider.list_contact:
        contact = contact.split(',')[:-1]
        try:
            name = permit[contact[0]]
            city = permit[contact[1]]
            state = permit[contact[2]]
            zipcode = permit[contact[3]]
            to_contact.append({"name": name, "location": {"city": city, "state": state, "zipcode": zipcode}})
        except:
            return to_contact


class PermitSpider(scrapy.Spider):
    name = "permit"
    list_contact = [gen_contact(x) for x in range(15)]
    str_contact = ' '.join(map(str, list_contact))
    field = 'permit_,permit_type,application_start_date,issue_date,street_number,street_direction,street_name, ' \
            f'suffix,work_description,total_fee,reported_cost,{str_contact[:-1]}'
    not_null = 'permit_ IS NOT NULL AND issue_date IS NOT NULL AND street_number IS NOT NULL AND street_direction  IS ' \
               'NOT NULL AND street_name IS NOT NULL AND suffix  IS NOT NULL '
    limit = '20'
    offset = '20'
    start_urls = [
        f"https://data.cityofchicago.org/api/id/ydr8-5enu.json?$select={field}&$where={not_null}&$limit={limit}&$offset={offset}"]

    def parse(self, response, **kwargs):
        permits = json.loads(response.body)

        for permit in permits:
            permit_loader = ItemLoader(PermitItem(), response)
            permit_loader.default_output_processor = TakeFirst()
            # permit_loader = ItemLoader(item=PermitItem, selector=permit)
            permit_loader.add_value('permit_number', permit['permit_'])
            permit_loader.add_value('permit_type', permit['permit_type'])
            permit_loader.add_value('application_date', permit['application_start_date'])
            permit_loader.add_value('issue_date', permit['issue_date'])
            permit_loader.add_value('street', permit['street_number'] + " " + permit['street_direction'] + " " + \
                                    permit['street_name'] + " " + permit['suffix'])
            permit_loader.add_value('city', "Chicago")
            permit_loader.add_value('state', "Illinois")
            permit_loader.add_value('description', permit['work_description'])
            permit_loader.add_value('fee', permit['total_fee'])
            permit_loader.add_value('cost', permit['reported_cost'])

            to_contact = parse_contact(permit)
            permit_loader.add_value('contacts', to_contact)

            yield permit_loader.load_item()
