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
    def __init__(self, name, kilometers, car_list: list):
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
        for self.car in self.car_list:
            while self.car.kuljettu_matka < self.kilometers:

                self.hours_passed()
                print(self.print_stats())
                print("-" * 75)
        print("Race finished!")
        return True



maxima_velocidad = random.randint(100, 200)
cambio_velocidad = random.randint(-10, 15)

maxima_velocidad2 = random.randint(100, 200)
cambio_velocidad2 = random.randint(-10, 15)


auto_1 = Auto(f"Zula", maxima_velocidad, cambio_velocidad, 0)
auto_2 = Auto(f"Fidel", maxima_velocidad2, cambio_velocidad2, 0)


carrera = Race("Grand Demolition Derby", 8000, [auto_1, auto_2])


carrera.race_finished()
