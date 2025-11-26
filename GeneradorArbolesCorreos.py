import random

class GeneradorArbolesCorreos:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def generar_arboles(self, hojas):

        if len(hojas)== 1:  #si solamente es una hojda
            return str(hojas[0])
        
        #dividimos aleatoriamente las hojas en dos mitades
        random.shuffle(hojas)
        mid = len(hojas) // 2

        izq = self.generar_arboles(hojas[:mid])
        der = self.generar_arboles(hojas[mid:])

        return f"({izq}, {der})"
    
    def generar_archivo(self, num_dias = 7, num_max_ofi = 255, peso_min = 1, peso_max = 10):

        with open(self.ruta_archivo, "w") as archivo:
            for _ in range(num_dias):
                num_oficinas = random.randint(2, num_max_ofi)   #num aleatorio de oficinas
                hojas = [random.randint(peso_min, peso_max) for _ in range(num_oficinas)]    #pesos aleatorios

                #construimos arbol binario
                arbol = self.generar_arboles(hojas)

                archivo.write(arbol + "\n")
            print(f"Archivo generado en: {self.ruta_archivo}")

def main():
        generador = GeneradorArbolesCorreos("arboles_correos.txt")
        generador.generar_archivo(num_dias=7, num_max_ofi=255, peso_min=1, peso_max=10)

if __name__ == "__main__":
    main()