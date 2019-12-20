from back_end import csv, writeInsert
from time import sleep
import os
import argparse

### MAIN PROGRAM ###

def run(args):
	t_name = args.t_name
	f_name = args.f_name
	out_name = args.out_name
	if writeInsert(f_name, t_name, out_name):
		print(f"Archivo SQL creado con éxito en {out_name}")
		sleep(1)
		os.system(out_name) # Corre el archivo creado 

def main():
	parser=argparse.ArgumentParser(description="Retorna una sentencia SQL enriquecida por un archivo CSV")
	parser.add_argument("-tb",help="Nombre de la Tabla en la que se insertarán los datos" ,dest="t_name", type=str, required=True)
	parser.add_argument("-in",help="Directorio y nombre del archivo .CSV" ,dest="f_name", type=str, required=True)	
	parser.add_argument("-out",help="Directorio y nombre del archivo .SQL" ,dest="out_name", type=str, required=True)	
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
