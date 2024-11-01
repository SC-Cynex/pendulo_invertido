import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def create_fis():
    angle = ctrl.Antecedent(np.arange(-15, 16, 1), 'angle')
    angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 1), 'angular_velocity')

    force = ctrl.Consequent(np.arange(-30, 31, 1), 'force')
    
    angle['left'] = fuzz.trapmf(angle.universe, [-15, -15, -7, 0])
    angle['center'] = fuzz.trimf(angle.universe, [-7, 0, 7])
    angle['right'] = fuzz.trapmf(angle.universe, [0, 7, 15, 15])
    
    angular_velocity['left'] = fuzz.trapmf(angular_velocity.universe, [-10, -10, -5, 0])
    angular_velocity['center'] = fuzz.trimf(angular_velocity.universe, [-5, 0, 5])
    angular_velocity['right'] = fuzz.trapmf(angular_velocity.universe, [0, 5, 10, 10])
    
    force['strong_left'] = fuzz.trapmf(force.universe, [-30, -30, -15, 0])
    force['weak_left'] = fuzz.trimf(force.universe, [-15, 0, 15])
    force['strong_right'] = fuzz.trapmf(force.universe, [0, 15, 30, 30])
    
    rules = [
        ctrl.Rule(angle['left'] & angular_velocity['left'], force['strong_left']),
        ctrl.Rule(angle['left'] & angular_velocity['center'], force['weak_left']),
        ctrl.Rule(angle['left'] & angular_velocity['right'], force['weak_left']),
        ctrl.Rule(angle['center'] & angular_velocity['left'], force['weak_left']),
        ctrl.Rule(angle['center'] & angular_velocity['center'], force['weak_left']),
        ctrl.Rule(angle['center'] & angular_velocity['right'], force['weak_left']),
        ctrl.Rule(angle['right'] & angular_velocity['left'], force['weak_left']),
        ctrl.Rule(angle['right'] & angular_velocity['center'], force['weak_left']),
        ctrl.Rule(angle['right'] & angular_velocity['right'], force['strong_right']),
    ]
    
    control_system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(control_system)
    return sim
