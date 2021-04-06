import random
class Poblacion:
    def __init__(self):
        self._largo_gen=10
        self._tamano_poblacion=10
        self.modelo=[1,1,1,1,1,2,2,2,2,2]
        self._numero_padres=3
        self._probabilidad_mutacion=0.2
    def crear_individuos(self, min, max):
        return [random.randint(min, max) for i in range(self._largo_gen)]
    
    def crear_poblacion(self):
        population= [Poblacion.crear_individuos(1,10) for i in range(self._tamano_poblacion)]
        print(f'poblacion inicial = {population}')
        Poblacion.modificar_poblacion(population)
    def calcular_fitness(self, individuo):
        fitness=0
        for i in range(self._largo_gen):
            if individuo[i]==self.modelo[i]:
                fitness+=1
        return fitness
    
    def elegir_poblacion(self, population, accuracy):
        new_population=[]
        for i in range (population-(self._numero_padres)):
            for i in sorted(accuracy.values()):
                new_population.append(accuracy.keys())
        population=new_population
        return(population)
    
    def mutacion(self, population):
        for individuo in (population): 
            for gen in range (len(individuo)):
                if random.random() <= self._probabilidad_mutacion:
                    individuo[gen]=random.randint(1,9)
                    while individuo[gen]==random.randint(1,9):
                        individuo[gen]=random.randint(1,9)
        return(population)

    def modificar_poblacion(population):
        accuracy={}
        for individuo in (population):
            accuracy[individuo]=(Poblacion.calcular_fitness(individuo))
        Poblacion.elegir_poblacion(population, accuracy)
        Poblacion.mutacion(population)
        print(f'poblacion final = {population}')
        return (population)

if __name__=='__main__':
    population=Poblacion
    population.crear_poblacion()

    
