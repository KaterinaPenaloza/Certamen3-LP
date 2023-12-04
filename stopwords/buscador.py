class Buscador:
    def __init__(self, indice_invertido):
        self.indice_invertido = indice_invertido

    def cargar_indice(self, ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) == 2:
                    termino, url = partes
                    if termino not in self.indice_invertido:
                        self.indice_invertido[termino] = set()
                    self.indice_invertido[termino].add(url)

    def buscar(self, consulta):
        terminos = consulta.split()
        resultados_parciales = [set(self.indice_invertido.get(termino, [])) for termino in terminos]
        if not all(resultados_parciales):
            return []
        resultado_final = self.intersectar_listas(resultados_parciales)
        return resultado_final

    def intersectar_listas(self, listas, indice=0):
        if indice == len(listas) - 1:
            return listas[indice]
        interseccion_actual = listas[indice].intersection(self.intersectar_listas(listas, indice + 1))
        return interseccion_actual

    def guardar(self, consulta, ruta_salida):
        resultados = self.buscar(consulta)
        with open(ruta_salida, 'w') as archivo_salida:
            if resultados:
                archivo_salida.write("Resultados de la búsqueda:\n")
                for url in resultados:
                    archivo_salida.write(url + '\n')
            else:
                archivo_salida.write("No se encontraron resultados para la consulta.\n")


if __name__ == "__main__":
    # Crear un objeto Buscador
    buscador = Buscador(indice_invertido={})
    # Cargar el índice invertido
    buscador.cargar_indice('indice_invertido.txt')
    # Archivos de entrada y salida
    ruta_consulta = "consulta.txt"
    with open(ruta_consulta, 'r') as archivo_consulta:
        consulta = archivo_consulta.read().strip()
    ruta_salida = "resultados_busqueda.txt"
    # Realizar la búsqueda
    resultados = buscador.buscar(consulta)
    # Guardar los resultados
    buscador.guardar(consulta, ruta_salida)
    # Mostrar los resultados
    if resultados:
        print("Resultados de la búsqueda:")
        for url in resultados:
            print(url)
    else:
        print("No se encontraron resultados.")

