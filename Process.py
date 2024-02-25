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
        print('%s arrives at %d' % (self.name, self.env.now))

        with os.ram.get(ram) as ram_req:
            yield ram_req
            print('%s gets %d ram at %d' % (self.name, ram, self.env.now))

            yield from self.ready(os)

        os.ram.put(ram)
        print('%s ends execution at %d' % (self.name, self.env.now))
    
    # Espera a ser atendido por el CPU
    def ready(self, os):
        with os.cpu.request() as cpu_req:
            yield cpu_req

            yield from self.running(cpu_req)
    
    # Ejecucción del proceso
    def running(self, cpu_req):
        print('%s starts execution at %d' % (self.name, self.env.now))

        while self.instructions > 0:
            for i in range(3):
                self.instructions -= 1

                if self.instructions == 0:
                    yield cpu_req
            
            yield self.env.timeout(1)