import time


class Nodo:
    def __init__(self, dato=None, izq=None, der=None):
        self.dato = dato
        self.der = der
        self.izq = izq

    def es_hoja(self):
        return self.izq is None and self.der is None

class contruccionArbol:

    def parser(self, s):
        s = s.strip()

        if s.isdigit():
            return Nodo(dato=int(s))
        
        if s[0] == '(' and s[-1] == ')':    #quitamos el parentesis exterior
            s = s[1:-1].strip()

        #buscamos las comas
        indice = self._coma_principal(s)

        izq = self.parser(s[:indice])
        der = self.parser(s[indice + 1:])

        nodoizq = izq
        nododer = der

        return Nodo(izq=nodoizq, der=nododer)
        
    
    def _coma_principal(self, s):
        nivel = 0

        for i, char in enumerate(s):
            if char == '(':
                nivel += 1
            elif char == ')':
                nivel -= 1
            elif char == "," and nivel == 0:
                return i
    
        raise ValueError("No se encontró una coma principal en la cadena.")
    
    def cargar_arboles_desde_archivo(self, ruta_archivo):
        arboles = []

        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    arbol = self.parser(linea)
                    arboles.append(arbol)
        
        return arboles
    
    def calc_peso_rutaRecursivo(self, nodo):
        
        if nodo.es_hoja():
            return nodo.dato, [nodo.dato], 1
        
        peso_izq, ruta_izq, calles_izq = self.calc_peso_rutaRecursivo(nodo.izq)
        peso_der, ruta_der, calles_der = self.calc_peso_rutaRecursivo(nodo.der)

        peso_total = peso_der + peso_izq
        num_calles = calles_der + calles_izq +1
        
        return peso_total, ruta_izq + ruta_der, num_calles
    

    def calc_peso_rutaIterativo(self, nodo):
        if nodo is None:
            return 0, [], 0
        
        peso_total = 0
        num_calles = 0
        stack = [nodo]

        while stack:
            actual = stack.pop()

            if actual.es_hoja():
                peso_total += actual.dato
                num_calles +=1

            #agregamos los nodos hijos al stack
            if actual.der is not None:  
                stack.append(actual.der)
                num_calles += 1
            
            if actual.izq is not None:
                stack.append(actual.izq)
                num_calles +=1
        return peso_total, [], num_calles

def main():
        constructor = contruccionArbol()
        arboles = constructor.cargar_arboles_desde_archivo("arboles_correos.txt")

        print(f"Se cargaron {len(arboles)} árboles")

        #Versión recursiva
        print("Rutas optimas Version Recursiva:")

        inicio = time.time()

        for i, arbol in enumerate(arboles):
            peso, ruta, calles = constructor.calc_peso_rutaRecursivo(arbol)

            print(f"Dia {i}: Ruta {ruta} - Calles {calles} - Peso {peso}")

        fin = time.time()

        tiempo_ejecucion = fin - inicio 

        print(f"Tiempo de ejecución: {tiempo_ejecucion:.10f} segundos")

        #Versión iterativa
        print("Rutas optimas Version Iterativa:")

        inicio = time.time()

        for i, arbol in enumerate(arboles):
            peso, ruta, calles = constructor.calc_peso_rutaIterativo(arbol)

            print(f"Dia {i}: Ruta {ruta} - Calles {calles} - Peso {peso}")

        fin = time.time()

        tiempo_ejecucion = fin - inicio 

        print(f"Tiempo de ejecución: {tiempo_ejecucion:.10f} segundos")


if __name__ == "__main__":
        main()

        