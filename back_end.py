''' Classes and global functions '''
import csv
from enum import Enum, auto
from os import read

# Si se puede cambiar a int retorna True, sino es falso
def is_int(var):
    try:
        int(var)
        return True
    except:
        return False

# Cuenta las rows
def row_count(f_name):
    with open(f_name) as in_file:
        return sum(1 for _ in in_file)

# Escribe archivo de texto
def write_insert(f_name, t_name, out_name):
    with open(f_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        f= open(out_name, "w+") 
        last_line_number = row_count(f_name)
        try:
            for row in csv_reader:
                if line_count == 0:
                    start_first = (f"INSERT INTO {t_name}(")
                    end_first = ") VALUES\n"
                    # Obtener los nombres de todas las columnas del CSV
                    column_names = ""
                    for idx, row_data in enumerate(row, start=1):
                        if idx == len(row): 
                            column_names += row_data
                        else:
                            column_names += row_data + ','
                    f.write(f"{start_first}{column_names}{end_first}")
                    line_count += 1 # Aumenta el index para el proximo ciclo
                else:
                    start = "("                  
                    content = ""
                    end = ")"
                    end_symbol = ""
                    for idx, row_data in enumerate(row, start=1):
                        if row_data == " " or row_data == "":
                            if idx == len(row): 
                                content += "null"
                            else:
                                content += "null,"
                        else:
                            # Si no es un numero le pone comillas
                            if is_int(row_data):
                                row_data = row_data
                            else:
                                row_data = "'" + row_data + "'"
                            # Agrega contenido al .txt
                            if idx == len(row): 
                                content += row_data                           
                            else:
                                content += row_data + ','          
                    if last_line_number == csv_reader.line_num:
                        end_symbol = ";"
                        f.write(f"{start}{content}{end}{end_symbol}")
                    else:
                        end_symbol = ",\n"
                        f.write(f"{start}{content}{end}{end_symbol}")
                        line_count += 1 # Aumenta el index para el proximo ciclo
            f.close()
            return True
        except (OSError, IOError) as error:
            print(error)
            return False


class SQL_FORMAT(Enum):
    SQL_SERVER = auto()
    PGSQL = auto()

class Querie():

    data_rows = []
    
    def __init__(self, file_name : str, table_name : str, output_file : str, sql_format : Enum ) -> None:
        self.file_name = file_name
        self.table_name = table_name
        self.output_file = output_file
        self.sql_format = sql_format

    def get_rows_from_file(self) -> list:
        ''' Abrir archivo csv y extraer data en lista ''' 
        with open(self.file_name, 'r', newline='') as file:
            has_header = csv.Sniffer().has_header(file.read(2048))
            file.seek(0)
            
            # NOTE: de momento solo envia lista vacia, tal vez enviar error?
            if not has_header:
                return []
            
            dialect= csv.Sniffer().sniff(file.read(), delimiters=',;')
            file.seek(0)

            reader = csv.reader(file, dialect)
            self.data_rows = [ row for row in reader ]
            return self.data_rows

    def format(self, field : str):
        if self.format == SQL_FORMAT.SQL_SERVER:
            return f'[{field}]'
        
        elif self.format == SQL_FORMAT.PGSQL:
             return f'"{field}"'
    
    def create_file_from_rows(self, rows) -> object:
        ''' Create the .sql file using the correct format, returns bool as result  '''
        if len(rows):
            with open(self.output_file, 'w+') as of:
                # get headers to use as column names
                query_columns = ''
                headers = rows[0]
                for idx, head in enumerate(headers):
                    query_columns += head + ', ' if idx != len(headers) - 1 else head
                #print("query_columns", query_columns)

                format(self.table_name) # ESta funcion deberia tomar el codigo de cada tipo para adaptarlo

                query = f"INSERT INTO {self.table_name} ({query_columns}) VALUES\n"
                #print('final_query so far:', final_query)
                
                values_string = ''
                query_values = ''
                for row_data in rows:
                    if row_data == rows[0]: continue

                    # TODO: Esto no maneja date types ni booleans ? probar ese tipo de casos
                    # TODO: Aqui encapsular una funcion que revise todos los posibles data types
                    for idx, value in enumerate(row_data): # da formato segun si es un int o string
                        if idx != len(row_data) - 1:
                            values_string += f"{value}," if is_int(value) else f"'{value}',"
                        else:
                            values_string += f"{value}," if is_int(value) else f"'{value}',"

                    # BUG: Esto se esta sobrecargando en vez de hacer lo que deberia, revisar
                    query_values += f'({values_string}),\n'    
                    
                final_query_string = query + query_values
                of.write(final_query_string)
                return of # Retorna el objeto file
        else:
            return None # Retorna un objeto nulo