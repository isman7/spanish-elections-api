# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:58:23 2015

@author: isman7
"""

import requests
import json
from constants import *

class basic_info(object):
    
    def __init__(self, name, input_dict):
        self.__dict__ = input_dict
        self.name = name
        
    def __repr__(self):
        return 'Info Object for eldiarioes-api'

class party(object):
    
    def __init__(self):
        self.info = basic_info('', {})        
    
    def __repr__(self):
        return 'Party Object for eldiarioes-api'
        
class district(object): 
    
    def __init__(self, name, decoded_json):
        #print decoded_json
        self.info = basic_info(name, decoded_json[u'Informaci\xf3n general:'])
    
    def __repr__(self):
        return 'Distric Object for eldiarioes-api'


class api_client(object):
    """
    api_client: will download all data related with the elections that are defined at
    the info of the analyzer object. 
    
    """    
    def get_result_by_district(self):
        return 1

    def get_results_by_party(self):
        return 1
        
        
    def get_results_all_districts(self):
        
        districts = []
        for local_district in DICT_OF_DISTRICTS:
            local_URL = '/'.join([BASE_URL,
                                  LIST_OF_CHAMBERS[0],
                                  LIST_OF_ELECTIONS[-1],
                                  DICT_OF_DISTRICTS[local_district]]) + '.' + FILE_API[0]
            #print local_URL
            local_json = json.loads(requests.get(local_URL).content)                      
            districts.append(district(local_district, local_json))
        
        self.old_districts = districts                          
        return districts

    def get_results_all_parties(self):
        return 1

    def __init__(self, info=basic_info('', {})):
        self.info = info
    
    def __repr__(self):
        return 'Client for making request to JSON api'
            

class analyzer(object):
    
    def __init__(self):
        
        self.info = basic_info('', {})
        self.api_client = api_client(info = self.info)
        self.districts = self.api_client.get_results_all_districts()        
        self.parties = self.api_client.get_results_all_parties()
        
    def __repr__(self):
        return 'Analyzer Object for eldiarioes-api'
        