""" Usar este .py para Construir data falsa csv simple """
import csv
from random import choice, randint
from pprint import pprint

# BUG: NO DETECTA HEADERS el csv_to_sql al intentar leer el data dummy

# NOTE: al parecer esto ocurre porque el header no es muy claro teniendo tanta data,
# una buena solucion es la consistencia de los datos derivados de cada header de columna,
# si se soluciona el problema de generar la data de manera consistente, se arregla el BUG 

# TODO: Esto "funciona", pero los datos en las rows de values son inconsistentes,
# en la misma columna BOOL deberian ser todos BOOL, pero diferentes valores
FAKE_DATA_TEMPLATE = {
    "HEADER_STRING" : "string",
    "HEADER_INT" : 999,
    "HEADER_DATE" : "01-01-2020",
    "HEADER_BOOL" : True,
}


def get_random_key() -> str:

    random_key = choice(list(FAKE_DATA_TEMPLATE.keys()))
    return random_key

    # random_value = fake_data_lookup[choice(list(fake_data_lookup.keys()))]
    # for key, value in fake_data_lookup.items():
    #     if random_value == value:
    #         random_key = key
    # return random_key

def make_data(cols : int, rows : int) -> None:
    with open('../test_files/mockup_data.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        column_headers = [ get_random_key() for i in range(cols) ] # gets a bunch of random keys
        # pprint(column_headers)
        writer.writerow(column_headers) # writes the column row
        
        for i in range(rows):
            writer.writerow( [ FAKE_DATA_TEMPLATE[col] for col in column_headers ] )
            
        # for row in range(rows):
        #     if row == 0: writer.writerow([el[0] for el in elements]) # header 
        #     writer.writerow([el[1] for el in elements])# row 

make_data(6, 50)
            

