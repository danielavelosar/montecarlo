import random
numero_padres=3
probabilidad_mutacion=0.2
modelo=[1,1,1,1,1,2,2,2,2,2]
class Poblacion:
    def __init__(self, largo_gen, tamano_poblacion):
        self.largo_gen=largo_gen
        self.tamano_poblacion=tamano_poblacion
    
    def crear_poblacion(self):
        population= []
        for i in range(self.tamano_poblacion):
            individual=[]
            for j in range(self.largo_gen):
                individual.append(random.randint(1,9))
            population.append(individual)
        print(f'poblacion inicial = {population}')
        for i in range(500):
            new_population=modificar_poblacion(population, self.largo_gen)
        print(f'poblacion final = {new_population}')

def calcular_accuracy(individuo, largo_gen):
    fitness=0
    for i in range(largo_gen):
        if individuo[i]==modelo[i]:
            fitness+=1
    return fitness
    
def combinar_padres(padre_1, padre_2,largo_gen, malo_1, malo_2):
    
    corte_gen=random.randint(0,largo_gen-1)
    malo_1[:corte_gen]= padre_1[:corte_gen]
    malo_1[corte_gen:]= padre_2[corte_gen:]
    malo_2[:corte_gen]= padre_2[:corte_gen]
    malo_2[corte_gen:]=padre_1[corte_gen:]
    return(malo_1, malo_2)

def sacar_padres(population, largo_gen):
    accuracy=[]
    for individuo in (population):
        accuracy.append(calcular_accuracy(individuo, largo_gen))
    if (max(accuracy)):
        
        return(individuo)

def quitar_menos_aptos(population, largo_gen):
    accuracy=[]
    for individuo in (population):
        accuracy.append(calcular_accuracy(individuo, largo_gen))
    for individuo in (population):
        if (calcular_accuracy(individuo, largo_gen))==(min(accuracy)):
            return (individuo)
        
        

def elegir_poblacion(population,largo_gen):
    old_population=population[::]
    new_population=population[::]
    padre_1=(sacar_padres(old_population,largo_gen))
    old_population.remove(padre_1)
    padre_2=(sacar_padres(old_population,largo_gen))
    #print(f'padres = {padre_1} y {padre_2}')
    malo_1=quitar_menos_aptos(old_population,largo_gen)
    old_population.remove(malo_1)
    malo_2=quitar_menos_aptos(old_population,largo_gen)
    hijo_1, hijo_2= combinar_padres(padre_1, padre_2, largo_gen, malo_1, malo_2)
    #print(f'hijos = {hijo_1} y {hijo_2}')
    new_population.append(hijo_1)
    new_population.append(hijo_2)
    new_population.remove(malo_1)
    new_population.remove(malo_2)   
    #print(f'malos = {malo_1} y {malo_2}')
    return(new_population) 

def mutacion( population):
    for individuo in (population): 
        for gen in range (len(individuo)):
            if random.random() <= probabilidad_mutacion:
                individuo[gen]=random.randint(1,9)
                while individuo[gen]==random.randint(1,9):
                    individuo[gen]=random.randint(1,9)
    return(population)



def modificar_poblacion(population, largo_gen):
    #print(len(population))
    new_population=elegir_poblacion(population, largo_gen)
    new_population=mutacion(new_population)
    
    #print(len(new_population))
    return (population)
        

if __name__=='__main__':
    population=Poblacion(10,10)
    print(f'modelo = {modelo}')
    population.crear_poblacion()
