# # The input of a list of websites will be provided. 
# For each of the domains, it will be searched on Ahrefs, and then click on the Linked Domains(on bottom-left corner). 
# The list of linked domains will be extracted in CSV. 
# The list of domains will now be searched on GoDaddy bulk domain search tool, and check the availability. 
# Extract the available domains from GoDaddy in CSV. 
# Search the domains on NameCheap bulk search tool to check the price. Omit those who are more costly than $100. 
# Download the list of available domains under $100 from namecheap in CSV format.  
# Put the list of domains from previous steps into Ahrefs Batch Analysis tool and sort them up as per DA. 
# Download the batch analysis data as per an ascending order of DR.

class App:
    def __init__(self):
        self.domain_list = []
        self.domain_list_with_price = []
        self.domain_list_with_price_and_availability = []
        self.domain_list_with_price_and_availability_and_da = []
        self.domain_list_with_price_and_availability_and_da_and_dr = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = []
        self.domain_list_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = []


class Domain(object):
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
class DomainWithPrice(object):
    def __init__(self, domain_name, price):
        self.domain_name = domain_name
        self.price = price
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and

class DomainWithPriceAndAvailability(object):
    def __init__(self, domain_name, price, availability):
        self.domain_name = domain_name
        self.price = price
        self.availability = availability
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
class DomainWithPriceAndAvailabilityAndDa(object):
    def __init__(self, domain_name, price, availability, da):
        self.domain_name = domain_name
        self.price = price
        self.availability = availability
        self.da = da
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        
class DomainWithPriceAndAvailabilityAndDaAndDr(object):
    def __init__(self, domain_name, price, availability, da, dr):
        self.domain_name = domain_name
        self.price = price
        self.availability = availability
        self.da = da
        self.dr = dr
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""

class DomainWithPriceAndAvailabilityAndDaAndDrAndUrl(object):
    def __init__(self, domain_name, price, availability, da, dr, url):
        self.domain_name = domain_name
        self.price = price
        self.availability = availability
        self.da = da
        self.dr = dr
        self.url = url
        self.domain_name_with_price = ""
        self.domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with_price_and_availability_and_da_and_dr_and_url = ""
        self.domain_name_with_price_and_availability_and_da_and_dr_and_url_and_domain_name_and_domain_name_with = ""

class DomainWithPriceAndAvailabilityAndDaAndDrAndUrlAndDomainName(object):
    
    
     