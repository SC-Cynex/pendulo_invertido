def evaluate_fitness(sim, angle, angular_velocity):
    sim.input['angle'] = angle
    sim.input['angular_velocity'] = angular_velocity
    sim.compute()
    force_output = sim.output['force']
    
    target_force = 0
    error = abs(force_output - target_force)
    return error
