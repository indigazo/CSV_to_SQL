''' Classes and global functions '''
import csv
from enum import Enum, auto
from os import read

# TODO: Separar a nivel de arquitectura el model (data), controler (back end) y view, todo lo que salga al client

# Enum, might not use
class SQL_FORMAT(Enum):
    SQL_SERVER  = auto()
    PGSQL       = auto()

# Si se puede cambiar a int retorna True, sino es falso
def is_num_type(var, type):
    try:
        if type == float:
            float(var)
            return True
        elif type == int:
            int(var)
            return True
    except:
        return False
    
# Cuenta las rows
def row_count(f_name):
    with open(f_name) as in_file:
        return sum(1 for _ in in_file)

# Obtiene todas las rows en una lista desde un archivo
def get_rows_from_file(file_name) -> list:
    data_rows = []
    with open(file_name, 'r', newline='') as file:
        has_header = csv.Sniffer().has_header(file.read(2048))
        file.seek(0)
        
        # NOTE: de momento solo envia lista vacia, tal vez enviar error?
        if not has_header:
            return []
        
        dialect = csv.Sniffer().sniff(file.read(), delimiters=',;')
        file.seek(0)

        # extract all the data on the file
        reader = csv.reader(file, dialect)
        data_rows = [ row for row in reader ]
        return data_rows

# Class to generate queries
class Querie():
    
    def __init__(self, rows : list, output_file_name : str) -> None:
        self.rows = rows
        self.output_file_name = output_file_name
    
    ''' Get the headers of the file on a list for easy use '''
    def get_header_row(self) -> list:
        if len(self.rows):
            return [ h for h in self.rows[0] ] 
    
    '''Checks if the string passed should be treated as a number, string, date or boolean (true, false)'''       
    def check_datatype(field : str) -> str:
        if field.lower() in ['true', 'false']:
            return field.lower()
        elif is_num_type(field, float):
            return float(field)
        elif is_num_type(field, int):
            return int(field)
        else:
            return field # is most likely a string
    
    def field_format(self, field : str) -> str:
        pass
    
    ''' Create the .sql file using the correct format, returns the file object or None  '''
    def get_querie_file_object(self) -> object:
        
        if len(self.rows):
            querie_header_fields = ""
            header_fields = self.get_header_row()
            
            with open(self.output_file_name, 'w+') as of:
                    
                # get headers to use as column names
                for idx, head in enumerate(header_fields):
                    querie_header_fields += head + ', ' if idx != len(header_fields) - 1 else head
                
                return querie_header_fields

                # format(self.table_name) # ESta funcion deberia tomar el codigo de cada tipo para adaptarlo

                # query = f"INSERT INTO {self.table_name} ({query_columns}) VALUES\n"
                # #print('final_query so far:', final_query)
                
                # values_string = ''
                # query_values = ''
                # for row_data in rows:
                #     if row_data == rows[0]: continue

                #     # TODO: Esto no maneja date types ni booleans ? probar ese tipo de casos
                #     # TODO: Aqui encapsular una funcion que revise todos los posibles data types
                #     for idx, value in enumerate(row_data): # da formato segun si es un int o string
                #         if idx != len(row_data) - 1:
                #             values_string += f"{value}," if is_int(value) else f"'{value}',"
                #         else:
                #             values_string += f"{value}" if is_int(value) else f"'{value}'"

                #     # BUG: Esto se esta sobrecargando en vez de hacer lo que deberia, revisar
                #     query_values += f'({values_string}),\n'    
                    
                # final_query_string = query + query_values
                # of.write(final_query_string)
                # return of # Retorna el objeto file
        else:
            return None # Retorna un objeto nulo

class SQLServer(Querie):
    
    def field_format(self, field : str):
        checked_field = self.check_datatype(field)
        return f'[{checked_field}]' # Default is SQL server

class PGSQL(Querie):

    def field_format(self, field : str):
        checked_field = self.check_datatype(field)
        return f'"{checked_field}"' # Default is SQL server