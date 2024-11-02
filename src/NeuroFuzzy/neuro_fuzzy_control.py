import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Definindo variáveis fuzzy de entrada
angulo = ctrl.Antecedent(np.arange(-90, 91, 1), 'angulo')
velocidade_angular = ctrl.Antecedent(np.arange(-10, 11, 1), 'velocidade_angular')

# Definindo variável fuzzy de saída
controle = ctrl.Consequent(np.arange(-10, 11, 1), 'controle')

# Conjuntos fuzzy para 'angulo'
angulo['esquerda'] = fuzz.trimf(angulo.universe, [-90, -45, 0])
angulo['vertical'] = fuzz.trimf(angulo.universe, [-45, 0, 45])
angulo['direita'] = fuzz.trimf(angulo.universe, [0, 45, 90])

# Conjuntos fuzzy para 'velocidade_angular'
velocidade_angular['esquerda'] = fuzz.trimf(velocidade_angular.universe, [-10, -5, 0])
velocidade_angular['parado'] = fuzz.trimf(velocidade_angular.universe, [-5, 0, 5])
velocidade_angular['direita'] = fuzz.trimf(velocidade_angular.universe, [0, 5, 10])

# Conjuntos fuzzy para 'controle'
controle['empurrar_esquerda'] = fuzz.trimf(controle.universe, [-10, -5, 0])
controle['neutro'] = fuzz.trimf(controle.universe, [-5, 0, 5])
controle['empurrar_direita'] = fuzz.trimf(controle.universe, [0, 5, 10])

# Definindo as regras fuzzy
rule1 = ctrl.Rule(angulo['esquerda'] & velocidade_angular['esquerda'], controle['empurrar_esquerda'])
rule2 = ctrl.Rule(angulo['esquerda'] & velocidade_angular['parado'], controle['empurrar_esquerda'])
rule3 = ctrl.Rule(angulo['esquerda'] & velocidade_angular['direita'], controle['neutro'])
rule4 = ctrl.Rule(angulo['vertical'] & velocidade_angular['esquerda'], controle['empurrar_esquerda'])
rule5 = ctrl.Rule(angulo['vertical'] & velocidade_angular['parado'], controle['neutro'])
rule6 = ctrl.Rule(angulo['vertical'] & velocidade_angular['direita'], controle['empurrar_direita'])
rule7 = ctrl.Rule(angulo['direita'] & velocidade_angular['esquerda'], controle['neutro'])
rule8 = ctrl.Rule(angulo['direita'] & velocidade_angular['parado'], controle['empurrar_direita'])
rule9 = ctrl.Rule(angulo['direita'] & velocidade_angular['direita'], controle['empurrar_direita'])

# Sistema de Controle Fuzzy
sistema_fuzzy = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
simulacao_fuzzy = ctrl.ControlSystemSimulation(sistema_fuzzy)

# Modelo de rede neural MLP
model = Sequential([
    Dense(10, input_dim=2, activation='relu'),
    Dense(10, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse')

# Dados simulados para treinamento (ângulo, velocidade angular)
train_data = np.array([
    [-45, -5], [0, 0], [45, 5],
    [-30, -2], [0, 1], [30, 2],
    [-15, 3], [15, -3]
])

# Controle desejado para cada par de entrada
train_labels = np.array([-1, 0, 1, -0.5, 0, 0.5, -0.3, 0.3])

# Treinamento da rede neural
model.fit(train_data, train_labels, epochs=200, verbose=1)

# Função para calcular a saída do sistema 
def neuro_fuzzy_control(angulo_val, vel_angular_val):
    # Parte Fuzzy
    simulacao_fuzzy.input['angulo'] = angulo_val
    simulacao_fuzzy.input['velocidade_angular'] = vel_angular_val
    simulacao_fuzzy.compute()
    
    fuzzy_output = simulacao_fuzzy.output['controle']
    
    # Parte Neural
    neural_input = np.array([[angulo_val, vel_angular_val]])
    neural_adjustment = model.predict(neural_input)[0][0]
    
    # Combinação dos resultados fuzzy e neural
    combined_output = fuzzy_output + neural_adjustment
    return combined_output

# Testando o sistema 
test_inputs = [[-45, -5], [0, 0], [45, 5]]
for angulo_val, vel_angular_val in test_inputs:
    output = neuro_fuzzy_control(angulo_val, vel_angular_val)
    print(f"Entrada (ângulo={angulo_val}, velocidade_angular={vel_angular_val}) -> Controle: {output}")
