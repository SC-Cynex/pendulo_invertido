import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def define_variables():
    angle = ctrl.Antecedent(np.arange(-90, 91, 1), 'angle')
    angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 1), 'angular_velocity')
    position = ctrl.Antecedent(np.arange(-10, 11, 1), 'position')
    car_velocity = ctrl.Antecedent(np.arange(-5, 6, 1), 'car_velocity')
    
    force = ctrl.Consequent(np.arange(-10, 11, 1), 'force')

    angle['left'] = fuzz.trimf(angle.universe, [-90, -45, 0])
    angle['vertical'] = fuzz.trimf(angle.universe, [-10, 0, 10])
    angle['right'] = fuzz.trimf(angle.universe, [0, 45, 90])

    angular_velocity['left'] = fuzz.trimf(angular_velocity.universe, [-10, -5, 0])
    angular_velocity['stopped'] = fuzz.trimf(angular_velocity.universe, [-1, 0, 1])
    angular_velocity['right'] = fuzz.trimf(angular_velocity.universe, [0, 5, 10])

    position['left'] = fuzz.trimf(position.universe, [-10, -5, 0])
    position['center'] = fuzz.trimf(position.universe, [-1, 0, 1])
    position['right'] = fuzz.trimf(position.universe, [0, 5, 10])

    car_velocity['left'] = fuzz.trimf(car_velocity.universe, [-5, -3, 0])
    car_velocity['stopped'] = fuzz.trimf(car_velocity.universe, [-1, 0, 1])
    car_velocity['right'] = fuzz.trimf(car_velocity.universe, [0, 3, 5])

    force['strong_left'] = fuzz.trimf(force.universe, [-10, -7, -3])
    force['slight_left'] = fuzz.trimf(force.universe, [-5, -3, 0])
    force['neutral'] = fuzz.trimf(force.universe, [-1, 0, 1])
    force['slight_right'] = fuzz.trimf(force.universe, [0, 3, 5])
    force['strong_right'] = fuzz.trimf(force.universe, [3, 7, 10])

    return angle, angular_velocity, position, car_velocity, force

def define_rules(angle, angular_velocity, position, car_velocity, force):
    rules = [
        ctrl.Rule(angle['left'] & angular_velocity['left'], force['strong_left']),
        ctrl.Rule(angle['left'] & angular_velocity['stopped'], force['slight_left']),
        ctrl.Rule(angle['left'] & angular_velocity['right'], force['neutral']),
        ctrl.Rule(angle['vertical'] & angular_velocity['left'], force['slight_left']),
        ctrl.Rule(angle['vertical'] & angular_velocity['stopped'], force['neutral']),
        ctrl.Rule(angle['vertical'] & angular_velocity['right'], force['slight_right']),
        ctrl.Rule(angle['right'] & angular_velocity['left'], force['neutral']),
        ctrl.Rule(angle['right'] & angular_velocity['stopped'], force['slight_right']),
        ctrl.Rule(angle['right'] & angular_velocity['right'], force['strong_right']),
        ctrl.Rule(position['left'] & car_velocity['left'], force['strong_right']),
        ctrl.Rule(position['left'] & car_velocity['stopped'], force['slight_right']),
        ctrl.Rule(position['left'] & car_velocity['right'], force['neutral']),
        ctrl.Rule(position['center'] & car_velocity['left'], force['slight_right']),
        ctrl.Rule(position['center'] & car_velocity['stopped'], force['neutral']),
        ctrl.Rule(position['center'] & car_velocity['right'], force['slight_left']),
        ctrl.Rule(position['right'] & car_velocity['left'], force['neutral']),
        ctrl.Rule(position['right'] & car_velocity['stopped'], force['slight_left']),
        ctrl.Rule(position['right'] & car_velocity['right'], force['strong_left']),
    ]
    return rules

def initialize_system():
    angle, angular_velocity, position, car_velocity, force = define_variables()
    rules = define_rules(angle, angular_velocity, position, car_velocity, force)
    pendulum_ctrl = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(pendulum_ctrl)

def compute_force(simulation, angle_value, angular_velocity_value, position_value, car_velocity_value):
    simulation.input['angle'] = angle_value
    simulation.input['angular_velocity'] = angular_velocity_value
    simulation.input['position'] = position_value
    simulation.input['car_velocity'] = car_velocity_value
    simulation.compute()
    return simulation.output['force']

simulation = initialize_system()
force = compute_force(simulation, -45, -5, -5, -2)
print(f"Força aplicada ao carro: {force}")
