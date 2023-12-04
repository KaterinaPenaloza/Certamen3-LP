# Certamen3-LP
Creación de una lista invertida para búsqueda de Documentos a partir del archivo **gov2_pages.dat**, en el cual cada línea del archivo contiene elementos separados por los caracteres “||” (doble barra vertical). Después de la última ocurrencia de “||” vienen los términos del contenido de cada página, y lo que lo antecede corresponde a su URL.

Por ejemplo:
http|| sgra|| jpl|| nasa|| gov|| JPL Sgra web Site JPL Sgra Web Site The US Space VLBI project web site has moved Click HERE to go to the new US Space VLBI project web site The following web pages are now available from this site Old US space VLBI project web site Project science web page Last updated Thu Sep 16 17 24 48 PDT 1999

http|| sgra|| jpl|| nasa|| gov|| --> url

el resto es el contenido de la página.


1) Preprocesamiento de los datos

* Reemplazar los || por ##, excepto el último

      sed 's/||/###/g; s/\(.*\)###\(.*\)/\1||\2/' gov2_pages.dat | awk -F '||' '{url=$1; content=$2; print url, content}' > preprocessed_data1.txt

    Salida:

      http### sgra### jpl### nasa### gov|| JPL Sgra web Site JPL Sgra Web Site The US Space VLBI project web site has moved Click HERE to go to the new US Space VLBI project web site The following web pages are now available from this site Old US space VLBI project web site Project science web page Last updated Thu Sep 16 17 24 48 PDT 1999

* Cambiar los ### por . excepto el último

      sed 's/###/\./g' preprocessed_data1.txt > preprocessed_data2.txt'

    Salida:
  
      http. sgra. jpl. nasa. gov|| JPL Sgra web Site JPL Sgra Web Site The US Space VLBI project web site has moved Click HERE to go to the new US Space VLBI project web site The following web pages are now available from this site Old US space VLBI project web site Project science web page Last updated Thu Sep 16 17 24 48 PDT 1999
  
* Sacar los espacios después de los puntos para que quede como solo una palabra

      awk '{gsub(/\. /, ".")} {print}' preprocessed_data2.txt > final_data.txt

     Salida:
  
      http.sgra.jpl.nasa.gov|| JPL Sgra web Site JPL Sgra Web Site The US Space VLBI project web site has moved Click HERE to go to the new US Space VLBI project web site The following web pages are now available from this site Old US space VLBI project web site Project science web page Last updated Thu Sep 16 17 24 48 PDT 1999
  
* Generar indices invertidos

      awk -f list.awk final_data.txt > indice_invertido.txt

    Esto generará un archivo llamado **indice_invertido.txt** en el cual cada término está asociada a su url

    Salida:

      from http.sgra.jpl.nasa.gov
      now http.sgra.jpl.nasa.gov
      web http.sgra.jpl.nasa.gov
      science http.sgra.jpl.nasa.gov
      this http.sgra.jpl.nasa.gov
      new http.sgra.jpl.nasa.gov
      here http.sgra.jpl.nasa.gov
      site http.sgra.jpl.nasa.gov
  
2) Eliminar stopwords

* Con este script de python se eliminarán todas las stopwords de la lista y mostrará por la terminal las palabras que se eliminaron. Este archivo se guardará en un nuevo directorio llamado **stopwords**

       python3 stopwords.py
   
3) Consultas

* Primero debe editar el archivo **consultas.txt** con las palabras que quiere consultar, por ejemplo, project science
  
* Ejecutar el script de búsqueda

      python3 busqueda.py
* Esto generará como salida un archivo llamado **resultados_busqueda.txt** y se mostrará también por la terminal.

  Salida:
  
      h
