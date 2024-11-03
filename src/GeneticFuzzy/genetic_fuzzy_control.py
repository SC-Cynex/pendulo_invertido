from GeneticFuzzy.fuzzy_system import create_fis
from GeneticFuzzy.genetic_algorithm import generate_initial_population, evaluate_population, selection, crossover, mutate

def genetic_algorithm():
    sim = create_fis()
    population = generate_initial_population()
    
    for generation in range(30):
        population_fitness = evaluate_population(population, sim)
        
        best_chromosome, best_fitness = population_fitness[0]
        print(f"Versão: {generation + 1}, Melhor: {best_fitness}, Parâmetros: {best_chromosome}")
        
        new_population = []
        while len(new_population) < 10:
            parent1, parent2 = selection(population_fitness)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:10]
    
    best_chromosome, best_fitness = evaluate_population(population, sim)[0]
    print(f"Melhor solução encontrada: {best_fitness}, Parâmetros: {best_chromosome}")

if __name__ == "__main__":
    genetic_algorithm()
