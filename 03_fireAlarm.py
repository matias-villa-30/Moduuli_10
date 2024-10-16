class Hissi:
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
        print(f"You start at {self.counter} floor")
        self.piso_destino = piso_destino
        if self.counter <= self.piso_destino:
            self.floor_up()
        elif self.counter >= self.piso_destino:
            self.floor_down()

        return f"You are now at floor {self.counter}"

class Building:

    def __init__(self, alakerta, ylakerta, hissit):
        self.alakerta = alakerta
        self.ylakerta = ylakerta
        self.hissit = hissit

    def run_elevator(self, hissi_numero, piso_destino):
        self.alarma = input("Cause fire alarm: (yes/no): ")
        self.hissi_numero = hissi_numero
        self.piso_destino = piso_destino
        self.lista_ascensores = []

        for self.ascensor in range(0, self.hissit):
            self.lista_ascensores.append(self.ascensor+1)

        if self.alarma.lower() == "no":
            return f"You selected the elevator {self.lista_ascensores[self.hissi_numero-1]} and you are going to floor number {self.piso_destino}"
        elif self.alarma.lower() == "yes":
            return self.fire_alarm()

    def fire_alarm(self):

        for self.hissi in self.lista_ascensores:
            self.piso_destino = self.alakerta

        return f"All the elevators {self.lista_ascensores} are on floor {self.piso_destino} due to fire alarm"

ascensor = Building(0, 10, 8)
print(ascensor.run_elevator(4, 8))

