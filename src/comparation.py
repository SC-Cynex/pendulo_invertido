from FIS.fuzzy_control import initialize_system as initialize_fuzzy_system, compute_force
from GeneticFuzzy.genetic_fuzzy_control import genetic_algorithm
from NeuroFuzzy.neuro_fuzzy_control import neuro_fuzzy_control

def run_fuzzy_control(angle, angular_velocity, position, car_velocity):
    fuzzy_system = initialize_fuzzy_system()
    return compute_force(fuzzy_system, angle, angular_velocity, position, car_velocity)

def run_genetic_fuzzy_control():
    genetic_algorithm()

def run_neuro_fuzzy_control(angle, angular_velocity):
    return neuro_fuzzy_control(angle, angular_velocity)

def generate_report():
    print("Relatório Comparativo dos Sistemas de Controle")
    print("=============================================")
    print()

    # Dados de teste
    test_data = [
        (-45, -5, -5, -2),
        (0, 0, 0, 0),
        (45, 5, 5, 2),
    ]

    # Resultados e avaliação
    print("### Avaliação do Sistema Fuzzy ###")
    fuzzy_forces = [run_fuzzy_control(angle, ang_vel, pos, car_vel) for angle, ang_vel, pos, car_vel in test_data]
    for (angle, ang_vel, pos, car_vel), force in zip(test_data, fuzzy_forces):
        print(f"Entrada: Ângulo={angle}°, Velocidade Angular={ang_vel}, Posição={pos}, "
              f"Velocidade do Carro={car_vel} -> Força Calculada: {force:.2f}")

    print("\n### Avaliação do Sistema Genético-Fuzzy ###")
    run_genetic_fuzzy_control()
    print("O sistema Genético-Fuzzy foi otimizado.\n")

    print("### Avaliação do Sistema Neuro-Fuzzy ###")
    neuro_outputs = [run_neuro_fuzzy_control(angle, ang_vel) for angle, ang_vel, _, _ in test_data]
    for (angle, ang_vel), output in zip([(angle, ang_vel) for angle, ang_vel, _, _ in test_data], neuro_outputs):
        print(f"Entrada: Ângulo={angle}°, Velocidade Angular={ang_vel} -> Controle Calculado: {output:.2f}")

    print("\n### ANÁLISE ###")
    print("Critérios de Avaliação:")
    print("1. Precisão: Capacidade de calcular a força ou controle correto.")
    print("2. Adaptabilidade: Capacidade de se ajustar a mudanças.")
    print("3. Tempo de Resposta: Rapidez em fornecer a resposta.")
    print("4. Robustez: Capacidade de lidar com incertezas.")

    print("\n#### Comparação ####")
    print("- **Fuzzy**: Boa precisão, adaptação limitada e resposta rápida.")
    print("- **Genético-Fuzzy**: Melhor adaptação, mas maior custo computacional.")
    print("- **Neuro-Fuzzy**: Alta adaptabilidade e robustez, mas tempo de resposta inicial maior.")

    print("\n### Vantagens e Desvantagens ###")
    print("1. **Fuzzy**: Simplicidade e rapidez, mas menor adaptabilidade.")
    print("2. **Genético-Fuzzy**: Boa adaptação, mas alto custo computacional.")
    print("3. **Neuro-Fuzzy**: Alta adaptabilidade, mas necessidade de treinamento inicial.")

    print("\n### Conclusão ###")
    print("O sistema mais apropriado depende das condições e dos requisitos específicos:")
    print("- **Sistema Fuzzy**: Ideal para situações simples e de baixa variabilidade.")
    print("- **Sistema Genético-Fuzzy**: Útil para condições que requerem adaptação leve.")
    print("- **Sistema Neuro-Fuzzy**: Recomendado para ambientes com alta incerteza e necessidade de adaptabilidade constante.")
    print()

generate_report()
