from espacio_cultural import EspacioCultural

class DataSetEspaciosCulturales:
    def __init__(self, archivo_csv):
        self._archivo_csv = open(archivo_csv, encoding = "UTF-8")
        #Leemos la primera linea porque es sólo los nombres de las columnas
        self._archivo_csv.readline()
        self._lista_de_espacios = []
        for linea in self._archivo_csv:
            #Al iterar cada fila del archivo, creamos variables para poder crear
            #instancias de la clase EspacioCultural y las guardamos en la lista
            espacios = linea.split(",") #Dividimos la linea en campos
            nombre = espacios[3]
            calle = espacios[8]
            altura = espacios[9]
            barrio = espacios[10]
            funcion_principal = espacios[1]
            capacidad = espacios[27]
            self._lista_de_espacios.append(
                EspacioCultural(nombre, calle, altura, barrio, funcion_principal, capacidad))
        self._lista_de_espacios.sort() #Sorteamos basado en capacidad
        self._archivo_csv.close()
    
    def tamano(self):
        return len(self._lista_de_espacios) #Retorna la cantidad de espacios culturales
    
    def barrios(self):
        conjunto_barrios  = set()
        for espacios in self._lista_de_espacios:
            #Iteramos los espacios
            #Añadimos los barrios de los espacios culturales a un conjunto
            conjunto_barrios.add(espacios.barrio())
        return conjunto_barrios
    
    def espacios_del_barrio(self, barrio):
        lista_espacios_del_barrio = []
        for espacios in self._lista_de_espacios:
            if barrio == espacios.barrio():
                #Si el barrio del espacio cultural es el que queremos, lo
                #agregamos a la lista de espacios del barrio
                lista_espacios_del_barrio.append(espacios)
        return lista_espacios_del_barrio
    
    def espacio_por_nombre(self, nom):
        for espacios in self._lista_de_espacios:
            if nom == espacios.nombre():
                #Si el nombre que pasamos existe en la lista de espacios culturales,
                #devolvemos ese espacio
                return espacios
            
    def cantidad_por_barrio(self, capacidad):
        dicc_barrios = dict()
        barrios = self.barrios() #Creamos una variable con todos los barrios únicos
        for barrio in barrios:
            #Iteramos los barrios
            #Creamos elementos del diccionario para cada barrio
            dicc_barrios[barrio] = 0
        for espacios in self._lista_de_espacios:
            if int(espacios.capacidad()) >= capacidad:
                #Sí la capacidad del barrio es mayor a la requerida, la cantidad
                #de espacios en el barrio aumenta por una unidad
                dicc_barrios[espacios.barrio()] = dicc_barrios[espacios.barrio()] + 1
        return dicc_barrios
    
    def exportar_por_funcion(self, archivo_csv, funcion_principal):
        #Creamos el archivo en modo write y escribimos los nombres de las columnas
        archivo_nuevo = open(archivo_csv, "w")
        archivo_nuevo.write("NOMBRE,DIRECCION,BARRIO,CAPACIDAD_TOTAL\n")
        for espacio in self._lista_de_espacios:
            if (espacio.funcion_principal() == funcion_principal):
                #Si el espacio tiene la función principal requerida entonces 
                #creamos variables con los valores de las columnas requeridas
                #y los guardamos
                nombre = espacio.nombre()
                barrio = espacio.barrio()
                direccion = espacio.direccion()
                capacidad_total = espacio.capacidad()
                archivo_nuevo.write(
                    nombre + "," + direccion + "," + barrio + "," + capacidad_total + "\n")
        archivo_nuevo.close()