import pandas as pd
from mysql import connector
from dotenv import load_dotenv
import os
from datetime import datetime
import random
from random_location import generate_random_coordinates

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')

PAGES_FORMATS = {
    'Udemy' : {'date_format': '%Y-%d-%M', 'geo_format': 'GEO2', 'usr_doc': True},
    'Coursera': {'date_format': '%Y-%M-%d', 'geo_format': '', 'usr_doc': True},
    'Platzi' : {'date_format': '%M-%d-%Y', 'geo_format': 'GEO3', 'usr_doc': False},
    'Escuelita_Valores' : {'date_format': '%d-%M-%Y', 'geo_format': 'GEO3', 'usr_doc': False, 'JSON': True}
}

def generar_compras_dia(uni, qty=10, low_price=10, high_price =100):
    conn = connector.connect(user=username,
                         password=password,
                         host=host,
                         database=uni)

    cur = conn.cursor()
    cur.execute('SELECT id_cliente FROM clientes;')
    ids_usuarios = [ i[0] for i in cur.fetchall() ]


    cur.execute('SELECT id FROM cursos;') 	
    ids_cursos = [ i[0] for i in cur.fetchall() ]

    hoy = datetime.now().date()
    random.seed(hoy.day)
    insert_compra = '''INSERT INTO compras (id_curso, id_usuario, fecha, fecha_visualizacion, fecha_inicio, fecha_fin, interrupcion, longitud, latitud, calificacion, costo_servicio)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    for i in range(qty):
        random_usr = ids_usuarios[random.randint(0, len(ids_usuarios)-1)]
        random_curso = ids_cursos[random.randint(0, len(ids_cursos)-1)]
        random_calificacion = random.randint(1,10)
        random_precio = round(random.uniform(low_price, high_price), 2)
        #Para colombia
        latitude, longitude = generate_random_coordinates(-4.609943, 12.616667, -75.269943, -66.930057)

        vars = (random_curso, random_usr, hoy,hoy,hoy,hoy, None, longitude, latitude, random_calificacion, random_precio)

        cur.execute(insert_compra, vars)
        conn.commit()

    conn.close()
        
def generar_usuarios(uni, qty=1):
    pass

def generar_cursos(uni, qty=1):
    pass
 
def exportar_batch(uni):
    pass
    
if __name__ == "__main__":
    generar_compras_dia('Coursera')