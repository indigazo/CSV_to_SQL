from back_end import Querie, SQL_FORMAT
from back_end import csv, write_insert
from time import sleep
import os
import argparse

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

def main():
	q = Querie(
		'files/mockup_data.csv', 
		'Mockup', 
		'files/file.sql', 
		SQL_FORMAT.SQL_SERVER
	)
	rows = q.get_rows_from_file()
	if len(rows):
		print(rows)
		file = q.create_file_from_rows(rows)
		
		if file:
			print(f"file {file} created")
		
		else:
			#TODO: Manejar este error de manera mas elegante
			print("Error archivo no creado") 

	else:
		#TODO: Manejar este error de manera mas elegante
		print("Este .csv no contiene headers")

if __name__=="__main__":
	main()
