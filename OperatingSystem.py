import simpy

RAM = 100

class OperatingSystem:
    def __init__(self, env, ram):
        self.env = env
        self.ram = simpy.Container(env, capacity=ram, init=ram)
        self.cpu = simpy.Resource(env, capacity=1)