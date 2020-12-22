import scrapy
from enum import Enum
from scrapy.loader.processors import MapCompose
from dateutil.parser import parse


def parse_date(input_date):
    return parse(input_date).date()


def get_type(string):
    for permit_type in PermitType:
        if permit_type.value.lower() == string[9:].lower():
            return permit_type.value


def convert_float(string):
    return float(string)


class PermitItem(scrapy.Item):
    permit_number = scrapy.Field()
    permit_type = scrapy.Field(input_processor=MapCompose(get_type))
    application_date = scrapy.Field(input_processor=MapCompose(parse_date))
    issue_date = scrapy.Field(input_processor=MapCompose(parse_date))
    street = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()
    fee = scrapy.Field(input_processor=MapCompose(convert_float))
    contacts = scrapy.Field()
    cost = scrapy.Field(input_processor=MapCompose(convert_float))


class PermitType(Enum):
    PORCH_CONSTRUCTION = 'Porch Construction'
    ELECTRIC_WIRING = 'Electric Wiring'
    WRECKING_DEMOLITION = 'Wrecking Demolition'
    REINSTATE_REVOKED_PMT = 'Reinstate Revoked Pmt'
    SIGNS = 'Signs'
    NEW_CONSTRUCTION = 'New Construction'
    EASY_PERMIT_PROCESS = 'Easy Permit Process'
    RENOVATION_ALTERATION = 'Renovation Alteration'
    FOR_EXTENSION_OF_PMT = 'For Extension Of Pmt'
    SCAFFOLDING = 'Scaffolding'
    ELEVATOR_EQUIPMENT = 'Elevator Equipment'
