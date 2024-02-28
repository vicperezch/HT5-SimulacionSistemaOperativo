import simpy
import OperatingSystem as OS
import random

# Victor Pérez

# Parámetros de la simulación
RAM = 100
NUMBER_OF_CPU = 1
NUMBER_OF_PROCESSES = 10
CREATION_INTERVAL = 10
RANDOM_SEED = 25

# Función principal donde se ejecuta la simulación
def main():
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    os = OS.OperatingSystem(env, RAM, NUMBER_OF_CPU)
    env.process(os.process_generator(env, NUMBER_OF_PROCESSES, CREATION_INTERVAL))
    env.run()


if __name__ == "__main__":
    main()