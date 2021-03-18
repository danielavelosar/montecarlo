import random 
import math

    
def hierarchy(array):
    cluster={}
    other_array=array[::]
    for number  in array:
        other_array.remove(number)
        for other_number in other_array: 

            euclidean_distance= math.sqrt((number-other_number)**2)
            cluster[(other_number, number)]= euclidean_distance
        
        other_array.append(number)

            #print(cluster)
    least_distance(array, cluster)


def least_distance(array,cluster):
    valores=[]
    grupos=[]
    circulos=[]
    if len(array)==1:
        return 0
    
    for value in sorted (cluster.values()):
        valores.append(value)
        grupos.append(list(cluster.keys())[list(cluster.values()).index(value)])

        distancias= valores[0:len(array)]
        clusters=grupos[0:len(array)]
    endeograma(distancias,clusters, array)
           

def tipos( array):
    for posicion in array:
        if type(posicion) is tuple:
            #print('yes')
            media=sum(posicion)/len(posicion)
            array.remove(posicion)
            array.append(media)
    return array 
    
def eliminar_numeros_de_lista(numero_1, numero_2, array_rec, circulito):
    
    while len(array_rec)>=0:
        array_rec.remove(numero_1)
        array_rec.remove(numero_2)
        array_rec.append(circulito)
        #print(f'el array recuperado es  = {array_rec}')
        array_nuevo= tipos(array_rec)
        #print(f'array_nuevo es {array_nuevo}')
        return(array_nuevo)
    

def endeograma( valores, grupos, array): 
    new_array=array[::]
    array_rec=array
    arbolito={}
    while len (new_array ) >= 1:
        for posicion in range(len(new_array)-1):
            if min(valores)== valores[posicion]:
                distance=valores[posicion]
                circulito=grupos[posicion]
                numero_1,numero_2=grupos[posicion]
                arbolito[distance]=circulito    
                #print(f'numero1 = {numero_1} y numero_2 = {numero_2}')
                array_nuevo=eliminar_numeros_de_lista(numero_1, numero_2, array_rec, circulito)
                new_array.remove(new_array[posicion])
                print(f' el arbolito: {arbolito}')

                hierarchy(array_nuevo)
            if len(array_nuevo)==1:
                break

        

        break            






        
if __name__=='__main__':
    array=[random.randint(1,20) for i in range(10)] 
    print (array)
    print('el arbolito: {distancia:(cluster)}')
    hierarchy(array)




            

""" def main():
    while( len(array)<= 1):
        hierarchy(array) """
    
