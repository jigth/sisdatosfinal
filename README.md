# sisdatosfinal
Proyecto final sistemas intensivos en datos

## Ejemplo de uso del programa

Este ejemplo genera logs en la carpeta "/var/log/trainsdata/trips", la carpeta será nombrada según el primer argumento que se pasa al programa y el segundo argumento es usado para especificar la fuente desde donde se leen los datos que son luego puestos en los archivos .log

Se redirige la salida (los prints) a **/dev/null** para poder ejecutar uno o más scripts sin que hagan ruido y eviten el trabajo cómodo en la consola.

 sudo ./LogStreamer.py trips trips.txt > /dev/null & 
