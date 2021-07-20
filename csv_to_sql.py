import csv
import os
import argparse

from back_end import *
from time import sleep
from pprint import pprint

# front end useful functions
def get_class_from_dict(rows, file, table_name, key=SQL_FORMAT.SQL_SERVER):
	class_dict = {
		SQL_FORMAT.SQL_SERVER : SQLServer(rows, file, table_name),
		SQL_FORMAT.PGSQL : PGSQL(rows, file, table_name)
	}
	return class_dict.get(key, SQLServer(rows, file, table_name))

### MAIN PROGRAM ###

# def run(args):
# 	t_name = args.table_name
# 	f_name = args.csv_name
# 	out_name = args.sql_name
# 	if write_insert(f_name, t_name, out_name):
# 		print(f"Archivo SQL creado con éxito en {out_name}")
# 		sleep(1)
# 		os.system(out_name) # Corre el archivo creado 

# def main():
# 	parser=argparse.ArgumentParser(description="Retorna una sentencia SQL enriquecida por un archivo CSV")
# 	parser.add_argument("-tb",help="Nombre de la Tabla en la que se insertarán los datos" ,dest="table_name", type=str, required=True)
# 	parser.add_argument("-in",help="Directorio y nombre del archivo .CSV" ,dest="csv_name", type=str, required=True)	
# 	parser.add_argument("-out",help="Directorio y nombre del archivo .SQL" ,dest="sql_name", type=str, required=True)	
# 	parser.set_defaults(func=run)
# 	args=parser.parse_args()
# 	args.func(args)

# This is only proof of concept main, the final product uses argparse
def main():
    

    
	# file_rows = get_rows_from_file("test_files/MOCK_DATA.csv")
	# QuerieClass = get_class_from_dict(file_rows, "output_files/cosa.sql", "Personas", SQL_FORMAT.PGSQL) # no final argument means SQL server
	# fo = QuerieClass.get_querie_file_object()
	FileRows = get_rows_from_file("test_files/MOCK_DATA.csv")
	Querie = SQLServer(FileRows, "output_files/cosa.sql", "Personas")
	FileObject = Querie.get_querie_file_object()
 
 
	print(FileObject)

if __name__=="__main__":
	main()
