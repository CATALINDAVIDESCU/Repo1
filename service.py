from curs_6 import Car

class Service:
    list_car = []
    number_of_cars = 0
    price = 0

    def __init__(self):
        pass

    def setlist_car(self,list_car):
        self.list_car = list_car

    def get_number_of_cars(self):
        self.number_of_cars = len(self.list_car)
        return self.number_of_cars

    def setprice(self,price):
        self.price = price

    def calculatePrice(self):
        for x in self.list_car:
            if x.model == 'Logan':
                print('Pretul este 2500 lei')
                self.setprice(2500)
            elif x.model == 'Sandero':
                print('Pretul este 4000')
                self.setprice(4000)
            else:
                print('Pretul este 2500')
                self.setprice(2500)

car1 = Car('Logan','negru')
car2 =Car('Spring','gri')
car3 = Car('Duster','alb')
car4 = Car('Logan','mov')
service = Service()
service.setlist_car([car1,car2,car3,car4])
service.get_number_of_cars()
print(service.get_number_of_cars())
service.setlist_car([car1,car2,car3,car4])
print(service.get_number_of_cars())
service.calculatePrice()
service.get_number_of_cars()



