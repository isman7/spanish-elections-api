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
    def __str__(self):
        output = ''
        
        # Formating the dict printing fuction, isoliting 'name' property:        
        next_line = ': '.join(['Name', self.name])
        output = '\n'.join([output, next_line])
        for prop, value in self.__dict__.iteritems():
            #print prop, value            
            if prop is not 'name':
                prop = ' '.join(prop.split('_'))
                if isinstance(value, dict):
                    acc_keys = ''
                    for key, elem  in value.iteritems():
                        acc_keys = ', '.join([acc_keys, key])
                    next_line = ': '.join([prop, acc_keys[1:]])
                else:         
                    next_line = ': '.join([prop, str(value)])
                output = '\n'.join([output, next_line]) 
            
        return output

class party(object):
    
    def __init__(self, name, party_result):
        self.info = basic_info(name, {u'Complete_Name': party_result[u'Nombre completo']})        
        self.votes = long(party_result['Votos'])
    def __repr__(self):
        return 'Party Object for eldiarioes-api'
    def __str__(self):
        return ': '.join([self.info.name, str(self.votes)])
        
class district(object): 
    
    def __init__(self, name, decoded_json):
        #print decoded_json
        self.info = basic_info(name, decoded_json[u'Informaci\xf3n general:'])
        results = []
        for name, party_result in decoded_json[u'Escrutinio'].iteritems():
            results.append(party(name, party_result))
        self.results = results
        
    def __repr__(self):
        return 'District results of ' + self.info.name
    
    def __str__(self):
        output = 'District results of ' + self.info.name
        for party in self.results:
            output = '\n'.join([output, str(party)])
        return output



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
        for local_district in self.info.List_of_districts:
            local_URL = '/'.join([self.info.API_URL,
                                  self.info.List_of_chambers,
                                  self.info.List_of_elections,
                                  self.info.List_of_districts[local_district]])
            local_URL = '.'.join([local_URL, FILE_API[0]])
            print local_URL
            local_json = json.loads(requests.get(local_URL).content)                      
            districts.append(district(local_district, local_json))
        
        self.old_districts = districts  # TODO converting it in files or DB                        
        return districts

    def get_results_all_parties(self):
        return 1

    def __init__(self, info=basic_info('', {})):
        self.info = info
    
    def __repr__(self):
        return 'Client for making request to JSON api'
            

class analyzer(object):
    
    def __init__(self, 
                 name = 'Spanish election analyzer',
                 base_url = BASE_URL,
                 chamber = LIST_OF_CHAMBERS[0],
                 elections = LIST_OF_ELECTIONS[-1],
                 districts = DICT_OF_DISTRICTS):
        properties = {'API_URL': base_url,
                      'List_of_chambers': chamber,
                      'List_of_elections': elections,
                      'List_of_districts': districts,
                      'Number_of_districts': len(districts)}
        self.info = basic_info(name, properties)
        self.api_client = api_client(info = self.info)
        self.districts = self.api_client.get_results_all_districts()        
        self.parties = self.api_client.get_results_all_parties()
        
    def __repr__(self):
        return 'Analyzer Object for eldiarioes-api'
        
    def __str__(self):
        return str(self.info)
        