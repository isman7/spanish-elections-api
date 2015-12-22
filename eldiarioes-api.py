# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:58:23 2015

@author: isman7
"""

import requests
import json
from constants import *

class basic_info(object):
    
    def __init__(self):
        
        self.type = ''
        self.description = ''
        


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
        for district in DICT_OF_DISTRICTS:
            local_URL = '/'.join([BASE_URL,
                                  LIST_OF_CHAMBERS[0],
                                  LIST_OF_ELECTIONS[-1],
                                  DICT_OF_DISTRICTS[district]]) + '.' + FILE_API[0]
            print local_URL
            districts.append(json.loads(requests.get(local_URL).content))
        
        self.old_districts = districts                          
        return districts

    def get_results_all_parties(self):
        return 1

    def __init__(self, info=basic_info()):
        self.info = info
        


class party(object):
    
    def __init__(self):
        self.info = basic_info()
        
class district(object): 
    
    def __init__(self):
        self.info = basic_info()
    
class results(object):
    
    
    
    def __init__(self):
        
        self.base_URL = BASE_URL
        self.tipo_eleccion = u'congreso'
        self.fecha = u'diciembre-2015'
        self.comnidad_autonoma = ''
        self.provincia = ''
        self.municipio = ''
        self.results = self.get_results()
        
     
class analyzer(object):
    
    def __init__(self):
        
        self.info = basic_info()
        self.api_client = api_client(info = self.info)
        self.districts = self.api_client.get_results_all_districts()        
        self.parties = self.api_client.get_results_all_parties()
        
        