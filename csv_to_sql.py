import csv
import os
import argparse

from back_end import *
import time
from pprint import pprint

# front end useful functions
def get_class_from_dict(file, o_file, table_name, key=SQL_FORMAT.SQL_SERVER):
	class_dict = {
		SQL_FORMAT.SQL_SERVER : SQLServer(file, o_file, table_name),
		SQL_FORMAT.PGSQL : PGSQL(file, o_file, table_name)
	}
	return class_dict.get(key, SQLServer(file, o_file, table_name))

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
    

    
    # class setup    
	Querie = SQLServer(
		"test_files/MOCK_DATA.csv", 
  		"output_files/cosa.sql", 
    	"Personas"
	)
	file_object = Querie.get_querie_file_object() 
	print(file_object)

if __name__=="__main__":
	start_time = time.time()
	main()
	print("----Programa terminado en %s segundos" % (time.time() - start_time))
