import math
import random
from estadisticas import media, desviacion_estandar

def arrojar_agujas(numero_de_agujas ):
    distancias=[]
    dentro_circulo=0
    for agujas in range(numero_de_agujas):
        x=random.random()*random.choice([-1,1])
        y=random.random()*random.choice([-1,1])
        distancias.append (math.sqrt(x**2+y**2))
    for distancia in distancias:
        if distancia <= 1:
            dentro_circulo+=1
    return 4*dentro_circulo/numero_de_agujas

def estimado(numero_intentos, numero_agujas):
    intentos=[]
    for _ in range (numero_intentos):
        pi=arrojar_agujas(numero_agujas)
        intentos.append(pi)
    mu=round(media(intentos),5)
    sigma = round(desviacion_estandar(intentos),5)
    print(f' la media es {mu} con una desviación estándar de {sigma}')
    return(mu, sigma)

def main ( precision):
    numero_intentos=1000
    numero_agujas=1000

    sigma=precision #quiero tomar el 95% de probabilidad, regla empirica 

    while sigma >= precision/1.96:
        print(f' con {numero_agujas} agujas y una desviación de  {sigma}')
        media, sigma= estimado(numero_intentos, numero_agujas)
        numero_agujas *= 2

        
    return media 
    

if __name__ == "__main__":
    
    media=main(0.01)#este es el margen de error +-0.01


    




    



    
        

