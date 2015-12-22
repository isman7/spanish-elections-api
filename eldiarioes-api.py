# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:58:23 2015

@author: isman7
"""

import requests
import json

BASE_URL = u'http://elecciones.eldiario.es/'

LIST_OF_ELECTIONS = ['junio-1977',
                     'marzo-1979',
                     'octubre-1982',
                     'junio-1986',
                     'octubre-1989',
                     'junio-1993',
                     'marzo-1996',
                     'marzo-2000',
                     'marzo-2004',
                     'marzo-2008',
                     'noviembre-2011',
                     'diciembre-2015']
                     
LIST_OF_CHAMBERS = ['congreso',
                    'senado']


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
        
        final_URL = self.info.base_URL + self.info.tipo_eleccion + '/' + self.info.fecha + '.json'
        get_json = requests.get(final_URL)
        self.results = json.loads(get_json.content)
        return self.results

    def get_results_by_party(self):
        
        final_URL = self.info.base_URL + self.info.tipo_eleccion + '/' + self.info.fecha + '.json'
        get_json = requests.get(final_URL)
        self.results = json.loads(get_json.content)
        return self.results

    def get_results_all_districts(self):
        
        final_URL = self.info.base_URL + self.info.tipo_eleccion + '/' + self.info.fecha + '.json'
        get_json = requests.get(final_URL)
        self.results = json.loads(get_json.content)
        return self.results

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
        self.results = self.api_client.get_results_all_parties()
        self.districts = self.api_client.get_results_all_districts()
        