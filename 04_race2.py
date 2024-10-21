import random



class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def accelerate(self, velocidad):
        if velocidad > 0:
            self.tämänhetkinen_nopeus = min(self.huippunopeus, self.tämänhetkinen_nopeus + velocidad)
        else:
            self.tämänhetkinen_nopeus = max(0, self.tämänhetkinen_nopeus + velocidad)

    def drive(self, hours_drived):
        km_drived = hours_drived * self.tämänhetkinen_nopeus
        self.kuljettu_matka += km_drived

    def __str__(self):
        return f"{self.rekisteritunnus:10} | {self.huippunopeus:10} km/h | {self.tämänhetkinen_nopeus:15} km/h | {self.kuljettu_matka:15} km"

class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hours_passed(self):
        for car in self.car_list:
            speed_change = random.randint(-5, 15)
            car.accelerate(speed_change)
            car.drive(10)

    def print_stats(self):
        stats = []
        for car in self.car_list:
            stats.append(str(car))
        return "\n".join(stats)

    def race_finished(self):
        print("-" * 75 + "\n Grand Demolition Derby: Lap 1 \n" + "_" * 75)
        i = 2
        linea = "-" * 75
        while not any(car.kuljettu_matka >= self.kilometers for car in self.car_list):
            self.hours_passed()
            print(self.print_stats())
            print(f"{linea}\n Grand Demolition Derby: Lap {i} \n {linea}")
            i += 1

        return True



def main():
    autos = []
    for i in range(1, 11):
        autos.append(f"ABC-{i}")


    car_list = []


    for item in autos:
        maxima_velocidad = random.randint(100, 200)  # Random top speed for each car
        cambio_velocidad = random.randint(-10, 15)  # Initial random speed change
        car_list.append(Auto(item, maxima_velocidad, cambio_velocidad, 0))

    carrera = Race("Grand Demolition Derby", 8000, car_list)


    if carrera.race_finished():
        return True


print(main())




