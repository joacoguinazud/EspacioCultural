class EspacioCultural:
    def __init__(self, nombre, calle, altura, barrio, funcion_principal, capacidad):
        self._nombre = nombre
        self._calle = calle
        #La altura puede estar vacía. Sí lo está, le damos el valor -1.
        if altura == "":
            self._altura = -1
        else:
            self._altura = altura
        self._barrio = barrio
        self._funcion_principal = funcion_principal
        self._capacidad = capacidad
        
    def nombre(self):
        return self._nombre
    
    def direccion(self):
        return str(self._calle) + " " + str(self._altura)
    
    def barrio(self):
        return self._barrio
    
    def funcion_principal(self):
        return self._funcion_principal
    
    def capacidad(self):
        return self._capacidad
    
    def __repr__(self):
        return "<" + str(self._capacidad) + " PERSONAS@" + str(
            self._nombre) + "@" + str(self._barrio) + ">"
    
    def __lt__(self, other):
        #Creamos esta función auxiliar para poder sortear barrios por capacidad
        return self._capacidad < other._capacidad