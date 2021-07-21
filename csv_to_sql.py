import argparse
import time
from back_end import *
from pprint import pprint

# front end useful functions
def get_class_from_dict(file, o_file, table_name, key=SQL_FORMAT.SQL_SERVER):
	class_dict = {
		SQL_FORMAT.SQL_SERVER : SQLServer(file, o_file, table_name),
		SQL_FORMAT.PGSQL : PGSQL(file, o_file, table_name)
	}
	return class_dict.get(key, SQLServer(file, o_file, table_name))

### MAIN PROGRAM ###

def main_function_loop(args):
	print(args.sql_type)
	pass
	# t_name = args.table_name
	# f_name = args.csv_name
	# out_name = args.sql_name
	# if write_insert(f_name, t_name, out_name):
	# 	print(f"Archivo SQL creado con éxito en {out_name}")
	# 	sleep(1)
	# 	os.system(out_name) # Corre el archivo creado 

def arg_parser_entry():
	parser = argparse.ArgumentParser(description = "Retorna una sentencia SQL enriquecida por un archivo CSV")
	parser.add_argument("-i",help="ruta archivo .CSV" ,dest="csv_name", type=str, required=True)	
	parser.add_argument("-o",help="ruta salida archivo .SQL" ,dest="sql_name", type=str, required=True)	
	parser.add_argument("-t",help="Nombre de la Tabla en la que se insertarán los datos" ,dest="table_name", type=str, required=True)
	parser.add_argument("-s",help="Tipo de SQL en el que crear archivo. Si se deja en blanco es SQL server" ,dest="sql_type", type=str, required=False)
	parser.set_defaults(func = main_function_loop)
	args=parser.parse_args()
	args.func(args)

# This is only proof of concept main, the final product uses argparse
def test_main():

    # class setup
	Q = get_class_from_dict(
		"test_files/MOCK_DATA.csv", 
  		"output_files/cosa.sql", 
    	"Personas",
		SQL_FORMAT.SQL_SERVER
	)
	result = Q.generate_sql_file() 

	if result:
		print(f"Archivo 'output_files/cosa.sql' creado")
	else:
		print("No existian rows para generar archivo SQL")

if __name__=="__main__":
	start_time = time.time()

	# test_main()

	arg_parser_entry()

	print("** Programa terminado en %s segundos **" % (time.time() - start_time))
