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
        modificar_poblacion(population, self.largo_gen)

def calcular_fitness(individuo, largo_gen):
    fitness=0
    for i in range(largo_gen):
        if individuo[i]==modelo[i]:
            fitness+=1
    return fitness
    
def combinar_padres(padres):
    print(f'padres={len(padres)}')
    for i in range(2):
        posicion=random.randint(0,2)
        padre=padres[posicion]
        print(padre)

def elegir_poblacion(population, accuracy):
    new_population=[]
    for i in range (len(population)-(numero_padres)):
        for i in sorted(accuracy.keys()):
            new_population.append(accuracy.values())
        padres=random.sample(new_population, 1)      

    population=new_population
    print(f'padres = {padres}')
    combinar_padres(padres)
    return(population)

def mutacion( population):
    for individuo in (population): 
        for gen in range (len(individuo)):
            if random.random() <= probabilidad_mutacion:
                individuo[gen]=random.randint(1,9)
                while individuo[gen]==random.randint(1,9):
                    individuo[gen]=random.randint(1,9)
    return(population)

def modificar_poblacion(population, largo_gen):
    accuracy={}
    for individuo in (population):
        accuracy[(calcular_fitness(individuo, largo_gen))]= individuo
    elegir_poblacion(population, accuracy)
    mutacion(population)
    print(f'poblacion final = {population}')
    return (population)
        

if __name__=='__main__':
    population=Poblacion(10,10)
    population.crear_poblacion()
