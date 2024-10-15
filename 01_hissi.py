class Hissi():
    counter = 0
    def __init__(self, alakerta, ylakerta):
        self.alakerta = alakerta
        self.ylakerta = ylakerta

    def floor_up(self):
        if self.piso_destino > self.ylakerta:
            self.piso_destino = self.ylakerta

        while self.piso_destino > self.counter:
            self.counter += 1

    def floor_down(self):

        if self.piso_destino < self.alakerta:
            self.piso_destino = self.alakerta

        while self.counter > self.piso_destino:
            self.counter -= 1

    def go_to_floor(self, piso_destino):
        print(f"You are at {self.counter} floor")
        self.piso_destino = piso_destino
        if self.counter <= self.piso_destino:
            self.floor_up()
        elif self.counter >= self.piso_destino:
            self.floor_down()

        return f"You are at floor {self.counter}"


ascensor = Hissi(0, 10)

print(ascensor.go_to_floor(8))