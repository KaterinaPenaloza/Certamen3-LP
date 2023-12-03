#!/usr/bin/awk -f

BEGIN {
    FS = "\\|\\|";  # Escapar las barras verticales dobles para usarlas como delimitador
}

{
    url = $1;
    contenido = $0;
    gsub(/[[:punct:][:space:]]/, " ", contenido);  # Reemplazar puntuación y espacios con un solo espacio
    contenido = tolower(contenido);
    n = split(contenido, palabras, " ");
    
    # Utilizar un conjunto para rastrear términos únicos
    delete terminos_unicos;

    for (i = 1; i <= n; i++) {
        termino = palabras[i];
        if (termino != "" && index(url, termino) == 0) {
            terminos_unicos[termino] = 1;
        }
    }

    # Imprimir términos únicos junto con la URL
    for (termino in terminos_unicos) {
        print termino, url;
    }
}

