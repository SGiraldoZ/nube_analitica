import pandas as pd
from mysql import connector
from dotenv import load_dotenv
import os
from datetime import datetime
import random
from random_location import generate_random_coordinates
import json

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')

PAGES_FORMATS = {
    'Udemy' : {'date_format': '%Y-%d-%m', 'geo_format': 'GEO2', 'usr_doc': True, 'JSON': False},
    'Coursera': {'date_format': '%Y-%m-%d', 'geo_format': '', 'usr_doc': True, 'JSON': False},
    'Platzi' : {'date_format': '%m-%d-%Y', 'geo_format': 'GEO3', 'usr_doc': False, 'JSON': False},
    'Escuelita_Valores' : {'date_format': '%d-%m-%Y', 'geo_format': 'GEO3', 'usr_doc': False, 'JSON': True}
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
    conn = connector.connect(user=username,
                         password=password,
                         host=host,
                         database=uni)

    cur = conn.cursor()

    configuraciones = PAGES_FORMATS.get(uni)

    cities = pd.read_csv("cities.csv")

    insert_cliente = '''INSERT INTO clientes (ciudad, pais, n_doc_cliente, email_cliente, nombre_cliente, fecha_nacimiento, id_usuario)
                       VALUES (%s,%s,%s,%s,%s,%s,0);'''
    for i in range(qty):
        locacion_seleccionada = cities.iloc[random.randint(0,cities.shape[0]-1)]
        ciudad_selccionada = locacion_seleccionada['CIUDAD'+configuraciones['geo_format']]
        pais_selccionado = locacion_seleccionada['PAIS'+configuraciones['geo_format']]
        email = generate_random_email()
        doc_identidad = generate_random_id_number() if configuraciones['usr_doc'] else None
        nombre = generate_random_user_name()
        fecha_nacimiento = generate_random_birthday().date()

        vars = (ciudad_selccionada, pais_selccionado,doc_identidad, email,nombre, fecha_nacimiento)

        cur.execute(insert_cliente, vars)
        conn.commit()

    conn.close()


def generar_cursos(uni, qty=1):
    pass
 
def exportar_batch(uni):
    conn = connector.connect(user=username,
                         password=password,
                         host=host,
                         database=uni)
    
    df_compras = pd.read_sql("SELECT * FROM compras WHERE fecha > DATE_SUB(CURDATE(), INTERVAL 4 DAY);", conn)

    if not PAGES_FORMATS[uni]['JSON']:
      filename = 'output/'+uni+'_' + str(datetime.now().date()) + '.csv'
      df_compras.to_csv(filename, index=False, date_format=PAGES_FORMATS[uni]['date_format'])
    else:
      filename = 'output/'+uni+'_' + str(datetime.now().date()) + '.json'
      df_compras.to_json(filename, index=False, date_format=PAGES_FORMATS[uni]['date_format'])
       

def generate_random_email():
  domains = [
    'gmail.com',
    'hotmail.com',
    'yahoo.com',
    'outlook.com',
  ]

  domain = random.choice(domains)
  username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 10)))
  return f'{username}@{domain}'

def generate_random_birthday(min_year=1950, max_year=2005):
  """Genera una fecha de nacimiento aleatoria dentro de un rango de años especificado.

  Args:
    min_year: Año mínimo.
    max_year: Año máximo.

  Returns:
    Una fecha de nacimiento.
  """
  year = random.randint(min_year, max_year)
  month = random.randint(1, 12)
  day = random.randint(1, 28)
  return datetime(year, month, day)

def generate_random_id_number(length=10):
  """Genera un documento de identidad aleatorio solo con números y con una longitud especificada.

  Args:
    length: La longitud del documento de identidad.

  Returns:
    Un documento de identidad aleatorio.
  """

  while True:
    id_number = ''.join(str(random.randint(1, 9)) for _ in range(length))
    if id_number[0] != '0':
      return id_number

def generate_random_user_name():
  """Genera un nombre aleatorio de la forma `user+5_digitos`.

  Returns:
    Un nombre aleatorio de la forma `user+5_digitos`.
  """

  # Nombre de usuario.
  user_name = "user"

  # Genera 5 dígitos aleatorios.
  digits = "".join(str(random.randint(0, 9)) for _ in range(5))

  # Devuelve el nombre de usuario con los 5 dígitos aleatorios.
  return user_name + digits

def exportar_params():
  df = pd.DataFrame(PAGES_FORMATS)
  df.to_json('output/params.json')
   
    
if __name__ == "__main__":
    # generar_cursos('Coursera')
    generar_usuarios('Coursera', qty=20)
    #generar_compras_dia('Coursera')