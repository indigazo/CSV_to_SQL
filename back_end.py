import csv
import os

# Si se puede cambiar a int retorna True, sino es falso
def isInt(var):
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
def writeInsert(f_name, t_name, out_name):
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
                            if isInt(row_data):
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

