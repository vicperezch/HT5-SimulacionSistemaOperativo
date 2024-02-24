from random import expovariate

class Process:
    def __init__(self, env, instructions):
        self.env = env
        self.instructions = instructions
    
    def process_generator(self, env, number, interval):
        for i in range(number):
            t = expovariate(1.0 / interval)
            yield env.timeout(t)