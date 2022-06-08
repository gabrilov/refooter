# refooter

## Qué hace
Toma datos de un archivo csv y crea archivos HTML.

## Funcionamiento

En un documento de texto plano, colocar las marcas que señalan el lugar donde se insertarán las nuevas cadenas de texto.

Las marcas se asocian a una variable de la siguiente manera:

|Variable|Marca|
|--------|-----|
|marcas[0]|MarcaNombre|
|marcas[1]|MarcaCargo|
|marcas[2]|MarcaTelefono|
|marcas[3]|MarcaMail|

El fichero csv del que se toman las cadenas a insertar debe tener tantas columnas como número de marcas existen, y el número de registros será el que determine el número de archivos HTML que se crearán. Cada valor se insertará en su marca correspondiente siguiendo el orden en el que están dispuestos en el registro.

## El archivo CSV

El archivo csv debe usar comas para separar las columnas. Un ejemplo del archivo tal y como debe usarse por defecto sería:

```csv
 "Paco", "Director", "666 666 666 - 123 45 67 89", "mimail@mail.com"
 "Pepe", "Esbirro", "666 666 665 - 123 45 67 90", "explotado@mail.com"
```
