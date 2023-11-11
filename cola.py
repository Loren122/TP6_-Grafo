class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)
        
    def size(self):
        return len(self.__elementos)    

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.__elementos.pop(0)
            self.arrive(aux)
            return aux
