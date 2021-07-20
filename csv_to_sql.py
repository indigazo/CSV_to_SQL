import csv
import os
import argparse

from back_end import *
from time import sleep
from pprint import pprint

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
    
	def get_class(rows, file, key):
		class_dict = {
			SQL_FORMAT.SQL_SERVER : SQLServer(rows, file),
			SQL_FORMAT.PGSQL : PGSQL(rows, file)
		}
		querie_class = class_dict.get(key, SQLServer(rows, file))
		return querie_class
    
	file_rows = get_rows_from_file("test_files/MOCK_DATA.csv")
	querie = get_class(file_rows, "output_files/cosa.sql", SQL_FORMAT.SQL_SERVER)
	fo = querie.get_querie_file_object()
	print(fo)

if __name__=="__main__":
	main()
