import argparse
import time
from back_end import *

### MAIN PROGRAM ###
def main_function_loop(args):
	# check for all the values that can't be None
	if args.sql_file == None:
		args.sql_file = args.csv_file.replace(".csv",".sql")
  
	if args.table_name == None:
		args.table_name = "PlaceHolder" # TODO: Use the name of the sql_file

	if args.sql_type == None:
		args.sql_type = SQL_FORMAT.SQL_SERVER
  
	query = get_class_from_dict(args.csv_file, args.sql_file, args.table_name, args.sql_type)	
	result = query.generate_sql_file()
 	
	if result:
		print(f":: Archivo '{args.sql_file}' creado ::")
	else:
		print("No existian rows para generar archivo SQL")


def main():
	parser = argparse.ArgumentParser(description = "Retorna una sentencia SQL enriquecida por un archivo CSV")
	parser.add_argument("-i",
					help="Ruta y nombre del archivo .CSV",
     				dest="csv_file", 
         			type=str, required=True)	
	parser.add_argument("-o",
					help= "(Optional) Ruta de salida archivo .SQL. Si se deja en blanco se usara el misma nombre y ruta del archivo .CSV", 
					dest="sql_file",
					type=str, required=False)	
	parser.add_argument("-t",
					help="(Optional) Nombre de la Tabla en la que se insertarán los datos. Si se deja en blanco se usara el nombre del .CSV", 
     				dest="table_name", 
         			type=str, required=False)
	parser.add_argument("-s",
					help="(Optional) Tipo de SQL en el que crear archivo. Si se deja en blanco es SQL server",
     				dest="sql_type", 
         			type=str, required=False)
	parser.set_defaults(func = main_function_loop)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	start_time = time.time()
	main()
	print("** Programa terminado en %s segundos **" % (time.time() - start_time))
