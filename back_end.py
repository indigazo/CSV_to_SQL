''' Classes and global functions '''
import csv
from enum import Enum, auto
from os import close, read
from pprint import pprint

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

# Class to generate queries
class Querie():
    
    def __init__(self, file : list, output_file_name : str, table_name : str) -> None:
        self.file = file
        self.output_file_name = output_file_name
        self.table_name = table_name
    
    ''' Get the headers of the file on a list for easy use '''
    def get_header_row(self, rows) -> list:
        if len(rows):
            return [ h for h in rows[0] ] 
        
    def get_rows_from_file(self) -> list:
        data_rows = []
        with open(self.file, 'r', newline='') as file:
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
        
    '''Checks if the string passed should be treated as a number, string, date or boolean (true, false)'''       
    def check_datatype(self, field : str) -> str:
        if field.lower() in ['true', 'false']:
            return field.lower()
        
        elif is_num_type(field, int):
            return int(field)
        
        elif is_num_type(field, float):
            return float(field)
        
        else:
            return field # is most likely a string
    
    ''' Each instance of this class should override this method, it formats a field with the correct bracket type '''
    def field_bracket_format(self, field : str) -> str:
        pass
    
    ''' Create the .sql file using the correct format, returns the file object or None  '''
    def generate_sql_file(self) -> bool:
        data_rows = self.get_rows_from_file()
        
        if len(data_rows):   
            query_header_fields = ""
            header_fields = self.get_header_row(data_rows)
            
            with open(self.output_file_name, 'w+') as of:
                
                # setup first part 
                for idx, head in enumerate(header_fields):
                    head = self.field_bracket_format(head)
                    query_header_fields += head + ', ' if idx != len(header_fields) - 1 else head
                
                query_setup = f"INSERT INTO {self.field_bracket_format(self.table_name)} ({query_header_fields}) VALUES\n"
                
                # devuelve una nueva lista con los datos ya formateados como corresponde 
                formatted_rows = [ list(map(self.check_datatype, row)) for idx, row in enumerate(data_rows) if idx != 0 ]
                close_chars = [",\n", ";"]
                final_query_string = query_setup
                
                for d_idx, data_rows in enumerate(formatted_rows):
                    new_row_to_add = ""
                    for idx, row_el in enumerate(data_rows):
                        new_row_to_add += f"{row_el}," if idx != len(data_rows) - 1 else f"{row_el}"
                    
                    f_char = close_chars[1] if d_idx == (len(formatted_rows) - 1) else close_chars[0]
                    final_query_string += f"({new_row_to_add})" + f_char
                
                of.write(final_query_string)
                return True
        else:
            return False # Retorna un objeto nulo

class SQLServer(Querie):
    
    def field_bracket_format(self, field : str):
        checked_field = self.check_datatype(field)
        return f'[{checked_field}]' # Default is SQL server

class PGSQL(Querie):

    def field_bracket_format(self, field : str):
        checked_field = self.check_datatype(field)
        return f'"{checked_field}"' # Default is SQL server