""" Usar este .py para Construir data falsa csv simple """
from random import choice, randint
import csv

# BUG: NO DETECTA HEADERS el csv_to_sql al intentar leer el data dummy

# NOTE: al parecer esto ocurre porque el header no es muy claro teniendo tanta data,
# una buena solucion es la consistencia de los datos derivados de cada header de columna,
# si se soluciona el problema de generar la data de manera consistente, se arregla el BUG 

# TODO: Esto "funciona", pero los datos en las rows de values son inconsistentes,
# en la misma columna BOOL deberian ser todos BOOL, pero diferentes valores

def get_random_key_value() -> tuple:
    
    fake_data_lookup = {
        "HEADER_STRING" : randint(10, 100),
        "HEADER_INT" : randint(10, 100),
        "HEADER_DATE" : randint(10, 100),
        "HEADER_BOOL" : randint(10, 100),
    }

    random_value = fake_data_lookup[choice(list(fake_data_lookup.keys()))]
    for key, value in fake_data_lookup.items():
        if random_value == value:
            random_key = key
    return (random_key, random_value)

def make_data(cols : int, rows : int) -> None:
    with open('../files/mockup_data.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in range(rows):
            elements = [ get_random_key_value() for i in range(cols) ]
            if row == 0: writer.writerow([el[0] for el in elements]) # header 
            writer.writerow([el[1] for el in elements])# row 

make_data(8, 20)
            

