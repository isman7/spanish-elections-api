# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:25:58 2015

@author: isman7
"""

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
                        u'Valencia':                'comunitat-valenciana/valencia',
                        u'Alicante':                'comunitat-valenciana/alicantealacant',
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
                        u'Castellón':               'comunitat-valenciana/castelloncastello',
                        u'Cantabria':               'cantabria/cantabria',
                        u'Valladolid':              'castilla-y-leon/valladolid',
                        u'Ciudad Real':             'castilla-la-mancha/ciudad-real',
                        u'Huelva':                  'andalucia/huelva',
                        u'León':                    'castilla-y-leon/leon',
                        u'Lleida':                  'catalunya/lleida',
                        u'Cáceres':                 'extremadura/caceres',
                        u'Albacete':                'castilla-la-mancha/albacete',
                        u'Burgos':                  'castilla-y-leon/burgos',
                        u'Salamanca':               'castilla-y-leon/salamanca',
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

