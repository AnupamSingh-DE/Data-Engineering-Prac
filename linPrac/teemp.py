import math

class TempConverter:
    def __init__(self,temperature):
        print(id(self))
        self.temperature = temperature
    @staticmethod
    def celcius_to_farahanite(temperature):
        return f"{((temperature * 9/5) + 32)} celcius_to_farahanite"
    @staticmethod
    def farahanite_to_celcius(temperature):
        return f"{(temperature - 32)*(5/9)} farahanite_to_celcius"

    @staticmethod
    def celcius_to_kelvin(temperature):
        return f"{(temperature + 273.15)} celcius_to_kelvin"

    @staticmethod
    def farahanite_to_kelvin(temperature):
        return f"{(temperature - 32)*(5/9)+273.15} farahanite_to_kelvin"

    @staticmethod
    def kelvin_to_farahanite(temperature):
        return f"{(temperature - 273.15)*(9/5)+32} kelvin_to_farahanite"
    


t1 = TempConverter(500)
print(id(t1))
print(TempConverter.celcius_to_farahanite(50))
print(t1.farahanite_to_celcius(t1.temperature))
print(t1.celcius_to_kelvin(t1.temperature))
print(t1.farahanite_to_kelvin(t1.temperature))
print(t1.kelvin_to_farahanite(t1.temperature))
