import csv
import os
import argparse

from pprint import pprint
import time
from back_end import Querie, SQL_FORMAT
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
    
	START_TIME = time.time() # for time measurements
	def time_elapsed():
		print("--- Program finished in %s seconds ---" % (time.time() - START_TIME))
    
	q = Querie(
		'test_files/mockup_data.csv', 
		'Mockup', 
		'files/file.sql', 
		SQL_FORMAT.SQL_SERVER
	)
	rows = q.get_rows_from_file()
	if len(rows):
		file = q.create_file_from_rows(rows)

		if file:
			print(f"file 'files/file.sql' created")
			time_elapsed()		

		else:
			#TODO: Manejar este error de manera mas elegante
			print("Error archivo no creado")
			time_elapsed()

	else:
		#TODO: Manejar este error de manera mas elegante
		print("Ocurrio un error obteniendo las rows")
		time_elapsed()

if __name__=="__main__":
	main()
