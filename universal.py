import csv
import mysql.connector
import random
import schedule
import time
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class Universal:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="universal"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def generate_view(self, usuario_id, noticia_id, fechaVisualizacion=None):
        interrupcion = random.randint(0, 1)
        
        # If 'fechaVisualizacion' is not provided, use the current date
        if fechaVisualizacion is None:
            today = datetime.today()
            fechaVisualizacion = today.strftime('%Y-%m-%d')
        else:
            # Ensure 'fechaVisualizacion' is in the correct format (yyyy-mm-dd)
            try:
                fechaVisualizacion = datetime.strptime(fechaVisualizacion, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Please provide 'fechaVisualizacion' in 'yyyy-mm-dd' format.")

        longitud = random.uniform(-180, 180)
        latitud = random.uniform(-90, 90)
        calificacion = random.randint(1, 5)
        costo = random.randint(1000, 100000)

        # Insert the generated data into the 'visualizacion' table
        insert_query = "INSERT INTO visualizacion (idUsuario, idNoticia, interrupcion, longitud, latitud, calificacion, costo, fechaVisualizacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (usuario_id, noticia_id, interrupcion, longitud, latitud, calificacion, costo, fechaVisualizacion)
        self.cursor.execute(insert_query, data)
        self.connection.commit()

        # Get the 'idVisualizacion' of the inserted data
        id_visualizacion = self.cursor.lastrowid

        view_data = {
            'idVisualizacion': id_visualizacion,
            'idUsuario': usuario_id,
            'idNoticia': noticia_id,
            'interrupcion': interrupcion,
            'fechaVisualizacion': fechaVisualizacion,
            'longitud': longitud,
            'latitud': latitud,
            'calificacion': calificacion,
            'costo': costo
        }

        return view_data

    def generate_data(self, user_ids, noticia_ids, day_batch_size, fechaVisualizacion=None):

        usuarios_data = []
        noticias_data = []
        visualizacion_data = []
        for i in range(day_batch_size):
            user_query = f"SELECT * FROM usuario WHERE idUsuario = {user_ids[i]}"
            self.cursor.execute(user_query)
            usuario = self.cursor.fetchone()

            if usuario: 
                usuarios_data.append(usuario)

            noticia_query = f"SELECT * FROM noticia WHERE idNoticia = {noticia_ids[i]}"
            self.cursor.execute(noticia_query)
            noticia = self.cursor.fetchone()

            if noticia:
                noticias_data.append(noticia)

            visualizacion_data.append(self.generate_view(user_ids[i], noticia_ids[i], fechaVisualizacion))

        return usuarios_data, noticias_data, visualizacion_data

    def create_new_day(self, day_batch_size, fechaVisualizacion=None):

        user_ids = [random.randint(1, 1000) for _ in range(day_batch_size)]
        noticia_ids = [random.randint(1, 1000) for _ in range(day_batch_size)]

        usuarios_data, noticias_data, visualizacion_data = self.generate_data(user_ids, noticia_ids, day_batch_size, fechaVisualizacion)

        # Print user data
        for user in usuarios_data:
            print(user)

        # Print news data
        for noticia in noticias_data:
            print(noticia)

        for visualizacion in visualizacion_data:
            print(visualizacion)

        return usuarios_data, noticias_data, visualizacion_data

    def generate_historical_data(self):
        # Get the current date
        today = datetime.today()

        # Generate data for the last 6 days, including today
        for i in range(1, 6):
            # Calculate the date for the current iteration (from today to 5 days ago)
            current_date = today - timedelta(days=i)

            day_batch_size = random.randint(20, 80)

            # Call create_new_day function with the current date
            self.create_new_day(day_batch_size, fechaVisualizacion=current_date.strftime('%Y-%m-%d'))

    def get_data_for_date(self, fecha):
        fecha = datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d')

        user_query = f"SELECT * FROM visualizacion WHERE fechaVisualizacion = '{fecha}'"
        self.cursor.execute(user_query)
        visualizacion_data = self.cursor.fetchall()

        usuarios_data = []
        noticias_data = []

        for visualizacion in visualizacion_data:
            usuario_id = visualizacion['idUsuario']
            noticia_id = visualizacion['idNoticia']

            # Fetch user data
            user_query = f"SELECT * FROM usuario WHERE idUsuario = {usuario_id}"
            self.cursor.execute(user_query)
            usuario = self.cursor.fetchone()
            if usuario:
                usuarios_data.append(usuario)

            # Fetch noticia data
            noticia_query = f"SELECT * FROM noticia WHERE idNoticia = {noticia_id}"
            self.cursor.execute(noticia_query)
            noticia = self.cursor.fetchone()
            if noticia:
                noticias_data.append(noticia)

        return usuarios_data, noticias_data, visualizacion_data

    def combine_data(self, usuarios_data, noticias_data, visualizacion_data):
        combined_data = []
        
        # Use zip to iterate over the arrays in parallel
        for usuario, noticia, visualizacion in zip(usuarios_data, noticias_data, visualizacion_data):
            combined_object = {}
            combined_object.update(usuario)
            combined_object.update(noticia)
            combined_object.update(visualizacion)
            combined_data.append(combined_object)
        
        return combined_data

    def generate_csv_for_date(self):
        today = datetime.today()

        day_batch_size = random.randint(20, 80)

        # Call create_new_day function with the current date
        self.create_new_day(day_batch_size, fechaVisualizacion=today.strftime('%Y-%m-%d'))

        csv_filename = f"universal_data_{today.strftime('%Y-%m-%d')}.csv"
        fieldnames = []  # Collect field names

        with open(csv_filename, mode='w', newline='') as file:
            # Create a CSV writer with the output file
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header row to the CSV file
            writer.writeheader()

            for i in range(0, 5):
                # Calculate the date for the current iteration (from today to 5 days ago)
                current_date = today - timedelta(days=i)

                # Call get_data_for_date to retrieve the data
                usuarios_data, noticias_data, visualizacion_data = self.get_data_for_date(fecha=current_date.strftime('%Y-%m-%d'))

                combined_data = self.combine_data(usuarios_data, noticias_data, visualizacion_data)

                # Collect and write usuario data
                for data in combined_data:
                    if not fieldnames:
                        fieldnames = data.keys()
                        writer.fieldnames = fieldnames
                        writer.writeheader()
                    writer.writerow(data)

if __name__ == "__main__":

    universal_instance = Universal()
    universal_instance.generate_csv_for_date()

    account_name = "your_account_name"
    account_key = "your_account_key"  # Or use a connection string
    container_name = "your_container_name"
    csv_file_path = "path_to_your_csv_file.csv"  # Path to your CSV file

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create a BlobClient for your CSV file
    blob_client = container_client.get_blob_client("destination_folder/your_csv_file.csv")

    # Upload the CSV file to Blob Storage
    with open(csv_file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"Uploaded {csv_file_path} to Azure Blob Storage.")