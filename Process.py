import random

# Victor Pérez
# Clase que modela un proceso que llega al sistema operativo y se ejecuta
class Process:

    # Constructor
    def __init__(self, env, name, instructions):
        self.env = env
        self.name = name
        self.instructions = instructions


    # Llegada del proceso al sistema operativo
    def new(self, ram, os):
        print("{:.2f} - {} arrives".format(self.env.now, self.name))

        # Solicita la cantidad de ram necesaria
        with os.ram.get(ram) as ram_req:
            yield ram_req
            print("{:.2f} - {} gets {} ram".format(self.env.now, self.name, ram))

            # Se mantiene en cola hasta terminar sus instruccciones
            while(self.instructions > 0):
                yield from self.ready(os)

                # Operaciones de entrada/salida
                if self.instructions > 0 and random.randint(1, 2) == 1:
                    print("{:.2f} - {} is waiting".format(self.env.now, self.name))
                    yield self.env.timeout(2)

        os.ram.put(ram)
        print("{:.2f} - {} ends execution".format(self.env.now, self.name))
    

    # Espera a ser atendido por el CPU
    def ready(self, os):
        with os.cpu.request() as cpu_req:
            yield cpu_req

            yield from self.running()
    

    # Ejecución del proceso
    def running(self):
        print("{:.2f} - {} starts execution with {} instructions remaining".format(self.env.now, self.name, self.instructions))

        self.instructions -= 3

        # Proceso terminado
        if self.instructions < 0:
            return
    
        yield self.env.timeout(1)