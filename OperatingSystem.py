import simpy
import random
from Process import *

# Victor Pérez
# Clase que representa el sistema operativo
class OperatingSystem:

    # Constructor
    def __init__(self, env, ram, cpu_number, seed):
        self.env = env
        self.ram = simpy.Container(env, capacity=ram, init=ram)
        self.cpu = simpy.Resource(env, capacity=cpu_number)
        self.seed = seed
    
    # Generador de procesos
    def process_generator(self, env, number, interval):
        random.seed(self.seed)

        for i in range(number):
            p = Process(env, 'P%d' % i, 10)
            env.process(p.new(random.randint(1, 10), self))

            t = random.expovariate(1.0 / interval)
            yield env.timeout(t)