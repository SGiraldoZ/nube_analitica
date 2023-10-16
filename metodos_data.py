from datetime import datetime
import pandas as pd


PAGES_FORMATS = {
    'Udemy' : {'date_format': '%Y-%d-%M', 'geo_format': 'GEO2', 'usr_doc': True},
    'Coursera': {'date_format': '%Y-%M-%d', 'geo_format': '', 'usr_doc': True},
    'Platzi' : {'date_format': '%M-%d-%Y', 'geo_format': 'GEO3', 'usr_doc': False},
    'Escuelita_Valores' : {'date_format': '%d-%M-%Y', 'geo_format': 'GEO3', 'usr_doc': False, 'JSON': True},


}

if __name__ == '__main__':
    
