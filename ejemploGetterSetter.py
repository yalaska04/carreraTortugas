class ClaseConGetterYSetter:
    def __init__(self):
        self.__propiedad_privada = None
    
    # Getter/setter por separado:     
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    # Getter/setter en conjunto: 
    def propiedadPrivada(self, valor = None):
        if valor == None:
            return self.__propiedad_privada
        else:
            self.__propiedad_privada = valor
            
    def __str__(self):
        return 'ClaseConGetterYSetter con propiedadPrivada -> {}'.format(self.__propiedad_privada)
        
if __name__ == '__main__':
    c = ClaseConGetterYSetter()