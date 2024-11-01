import random
from fitness import evaluate_fitness

POPULATION_SIZE = 10
GENERATIONS = 30
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7

def generate_initial_population():
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = {
            'angle_left': random.uniform(-15, -5),
            'angle_center': random.uniform(-5, 5),
            'angle_right': random.uniform(5, 15),
            'angular_velocity_left': random.uniform(-10, -3),
            'angular_velocity_center': random.uniform(-3, 3),
            'angular_velocity_right': random.uniform(3, 10)
        }
        population.append(chromosome)
    return population

def evaluate_population(population, sim):
    fitness_scores = []
    for chromosome in population:
        sim.input['angle'] = chromosome['angle_center']
        sim.input['angular_velocity'] = chromosome['angular_velocity_center']
        
        fitness = sum(evaluate_fitness(sim, a, v) for a in range(-10, 10, 5) for v in range(-5, 5, 5))
        fitness_scores.append((chromosome, fitness))
    return sorted(fitness_scores, key=lambda x: x[1])

def selection(population_fitness):
    total_fitness = sum(fitness for _, fitness in population_fitness)
    selection_probs = [(chromosome, fitness / total_fitness) for chromosome, fitness in population_fitness]
    selected = random.choices([c for c, _ in selection_probs], weights=[f for _, f in selection_probs], k=2)
    return selected

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = {**parent1, **{k: parent2[k] for k in list(parent2.keys())[crossover_point:]}}
        child2 = {**parent2, **{k: parent1[k] for k in list(parent1.keys())[crossover_point:]}}
        return child1, child2
    return parent1, parent2

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        key = random.choice(list(chromosome.keys()))
        chromosome[key] += random.uniform(-1, 1)
    return chromosome
