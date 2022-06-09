# refooter

Refooter toma datos de un archivo csv y crea archivos HTML.

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
 "Paco", "Director", "666 666 666", "123 45 67 89", "mimail@mail.com"
 "Pepe", "Esbirro", "666 666 665,, "explotado@mail.com"
```

## Los teléfonos

En caso de que un registro incluya dos teléfonos, se pueden disponer en horizontal o en vertical:

1. Si es horizontal los teléfonos se separan por un guión.
2. Si es vertical, cada teléfono está incluído en un bloque `<div>`.

Por defecto, la salida es en forma vertical. Si se quiere indicar en horizontal hay que agregar la opcioń `-H` o `--horizontal`

## Uso del comando

Opciones:

`-f --file`: Path del archivo HTML fuente, el modelo para crear las réplicas.

`-c --csv`: Path del archivo csv que contiene los datos a insertar.

`-o --output`: Nombre de la carpeta donde se guardarán los archivos generados. Por defecto el nombre es `resultado` y se crea en el mismo directorio donde se ejecute el comando.

`-H --horizontal`: disposición de los teléfonos. Vertical por defecto.

`-v --verbose`: Activar más información en la salida del comando.

Por ejemplo, queremos obtener copias de una plantilla HTML llamada `modelo.html` e insertar datos de un archivo csv, `datos.csv`, con los teléfonos en horizontal separados por un guión y que devuelva los archivos resultantes en una carpeta llamda `salida`. Todos los archivos necesarios se encuentran en el mismo directorio.

```shell
refooter -f modelo.html -c datos.csv -H -o salida
```