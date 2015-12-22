# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:58:23 2015

@author: isman7
"""

import requests
import json

BASE_URL = u'http://elecciones.eldiario.es'

FILE_API = ['json',
            'csv']

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

# orderen decereciente en tamaño:

                    
DICT_OF_DISTRICTS =    {u'Madrid':                  'madrid/madrid',
                        u'Barcelona':               'catalunya/barcelona',
                        u'Valencia':                'comunitat-valencia/valencia',
                        u'Alicante':                'comunitat-valencia/alicantealacant',
                        u'Sevilla':                 'andalucia/sevilla',
                        u'Málaga':                  'andalucia/malaga',
                        u'Cádiz':                   'andalucia/cadiz',
                        u'Bizkaia':                 'euskadi/bizkaia',
                        u'A Coruña':                'galicia/a-coruna',
                        u'Illes Balears':           'illes-balears/illes-balears',
                        u'Las Palmas':              'canarias/las-palmas',
                        u'Asturias':                'asturias/asturias',
                        u'Santa Cruz de Tenerife':  'canarias/santa-cruz-de-tenerife',
                        u'Zaragoza':                'aragon/zaragoza',
                        u'Pontevedra':              'galicia/pontevedra',
                        u'Granada':                 'andalucia/granada',
                        u'Tarragona':               'catalunya/tarragona',
                        u'Córdoba':                 'andalucia/cordoba',
                        u'Girona':                  'catalunya/girona',
                        u'Gipuzkoa':                'euskadi/gipuzkoa',
                        u'Toledo':                  'castilla-la-mancha/toledo',
                        u'Almería':                 'andalucia/almeria',
                        u'Badajoz':                 'extremadura/badajoz',
                        u'Jaén':                    'andalucia/jaen',
                        u'Navarra':                 'navarra/navarra',
                        u'Castellón':               'comunitat-valencia/castelloncastello',
                        u'Cantabria':               'cantabria/cantabria',
                        u'Valladolid':              'castilla-y-leon/valladolid',
                        u'Ciudad Real':             'castilla-la-mancha/ciudad-real',
                        u'Huelva':                  'castilla-la-mancha/huelva',
                        u'León':                    'castilla-y-leon/león',
                        u'Lleida':                  'catalunya/lleida',
                        u'Cáceres':                 'extremadura/caceres',
                        u'Albacete':                'castilla-la-mancha/albacete',
                        u'Burgos':                  'castilla-y-leon/burgos',
                        u'Salamanca':               'castilla-y-leon/salamanca/',
                        u'Lugo':                    'galicia/lugo',
                        u'Ourense':                 'galicia/ourense',
                        u'La Rioja':                'la-rioja/la-rioja',
                        u'Álava':                   'euskadi/alava',
                        u'Guadalajara':             'castilla-la-mancha/guadalajara',
                        u'Huesca':                  'aragon/huesca',
                        u'Cuenca':                  'castilla-la-mancha/cuenca',
                        u'Zamora':                  'castilla-y-leon/zamora',
                        u'Ávila':                   'castilla-y-leon/avila',
                        u'Palencia':                'castilla-y-leon/palencia',
                        u'Segovia':                 'castilla-y-leon/segovia',
                        u'Teruel':                  'aragon/teruel',
                        u'Soria':                   'castilla-y-leon/soria',
                        u'Ceuta':                   'ceuta/ceuta',
                        u'Melilla':                 'melilla/melilla'
                        }




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
                                  self.info.tipo_eleccion,
                                  DICT_OF_DISTRICTS[district],
                                  LIST_OF_ELECTIONS[-1]]) + '.' + FILE_API[0]
            
            districts.append(json.loads(requests.get(local_URL).content))
                                  
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
        
        