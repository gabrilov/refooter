#!/usr/bin/env python

import argparse
import csv
import os

output_folder = "resultado"
csv_file = "tabla.csv"
fuente = "modelo.html"

###### Procesamiento de parámetros ####
texto_ayuda = "Script que replica un archivo modificándolo con las cadenas que se especifiquen en un csv."

parser = argparse.ArgumentParser(description=texto_ayuda)


parser.add_argument("-f", "--file", help="Path del archivo a modificar ('modelo.html' por defecto)")
parser.add_argument("-c", "--csv", help="Path del archivo csv que contiene los datos ('tabla.csv' por defecto)")
parser.add_argument("-o", "--output", help="Nombre de la carpeta para los archivos de salida ('resultado' por defecto)")
parser.add_argument("-H", "--horizontal", help="Disposición de los teléfonos en horizontal con guión de separación", action='store_true')
parser.add_argument("-v", "--verbose", help="Imprime descripción de procesos del script", action='store_true')

args = parser.parse_args()

if args.output:
    output_folder = args.output

if args.csv:
    csv_file = args.csv

if args.file:
    fuente = args.file

# Crea el directorio de salida
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lee el archivo csv
with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

"""
Variable 'file':
index - dato - variable
-------------
0 - Nombre - marcaNombre
1 - Cargo - marcaCargo
2 y 3 - Telf. fijo y movil - marcaTelefono
3 - Mail - marcaMail
"""
#### Copia de réplicas ####
for linea in data:
    nombre = linea[0].split(' ')
    tlfPrincipal = f'+34 {linea[2][:3]} {linea[2][3:6]} {linea[2][6:]}'
    if len(nombre) > 1:
        nombre_archivo = f'{nombre[0]}-{nombre[1]}'
    else:
        nombre_archivo = f'{nombre[0]}'

    if os.path.exists(f'{output_folder}/{nombre_archivo}'):
        nombre_archivo = f'{nombre_archivo}-2'

    archivo_destino = open(f'{output_folder}/{nombre_archivo}.html', 'w')

    if not linea[3]:
        telefonos = tlfPrincipal
    else:
        tlfSecundario = f'+34 {linea[3][:3]} {linea[3][3:6]} {linea[3][6:]}'
        if args.horizontal:
            telefonos = tlfPrincipal + " - " + tlfSecundario 
        else:
            telefonos = f'{tlfPrincipal}</div><div>{tlfSecundario}'            
    with open(fuente, 'rt') as modelo:
        for line in modelo:
            archivo_destino.write(line.replace('marcaNombre', linea[0]).replace('marcaCargo', linea[1]).replace('marcaTelefono', telefonos).replace('marcaMail', linea[4]))
        if args.verbose:
            print(f'{output_folder}/{nombre_archivo} creado')

    archivo_destino.close()