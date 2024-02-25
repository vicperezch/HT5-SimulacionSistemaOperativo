import simpy
import OperatingSystem as OS

# Victor Pérez

# Parámetros de la simulación
RAM = 10
NUMBER_OF_CPU = 1
NUMBER_OF_PROCESSES = 5
CREATION_INTERVAL = 10
RANDOM_SEED = 78

# Función principal donde se ejecuta la simulación
def main():
    env = simpy.Environment()
    os = OS.OperatingSystem(env, RAM, NUMBER_OF_CPU, RANDOM_SEED)
    env.process(os.process_generator(env, NUMBER_OF_PROCESSES, CREATION_INTERVAL))
    env.run()


if __name__ == "__main__":
    main()