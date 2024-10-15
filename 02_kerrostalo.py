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
        print(f"You start at {self.counter} floor")
        self.piso_destino = piso_destino
        if self.counter <= self.piso_destino:
            self.floor_up()
        elif self.counter >= self.piso_destino:
            self.floor_down()

        return f"You are now at floor {self.counter}"

class Building():

    def __init__(self, alakerta, ylakerta, hissit):
        self.alakerta = alakerta
        self.ylakerta = ylakerta
        self.hissit = hissit

    def run_elevator(self, hissi_numero, piso_destino):
        self.hissi_numero = hissi_numero
        self.piso_destino = piso_destino
        self.lista_ascensores = []

        for self.ascensor in range(1, self.hissit):
            self.lista_ascensores.append(self.ascensor)

        return f"You selected the elevator {self.lista_ascensores[self.hissi_numero-1]} and you are going to floor number {self.piso_destino}"




print("Create new building")
edificio = int(input("Number of floors: "))
ascensores = int(input("Number of elevators: "))
ascensor_numero = int(input("Select the number of the elevators: "))
numero_edificio = int(input("Select the number of the floor you wanna go: "))
edificio = Building(0, edificio, ascensores)

print(edificio.run_elevator(ascensor_numero, numero_edificio))