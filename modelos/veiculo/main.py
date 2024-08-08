from carro import Carro
from moto import Moto

carro1 = Carro('Sandero', 'Renault', 4)
carro2 = Carro('Kwid', 'Renault', 2)
moto1 = Moto('Honda', 'Biz', 100)
moto2 = Moto('Honda', 'Dream', 110)

def main():
    print(carro1)
    print(carro2)
    print(moto1)
    print(moto2)

if __name__ == '__main__':
    main()