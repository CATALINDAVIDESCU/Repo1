# class Car:
#     __color = 'gri'
#     model = 'BMW'
#     def get_color(self):
#         return self.__color
#
#     def set_color(self,culoare_dorita):
#         self.__color = culoare_dorita
#         self.__mesaj(f'Culoarea a fost schimbata in {culoare_dorita}')
#     def __mesaj(self,mesaj):
#         print(mesaj)
#
# masina = Car()
# masina.set_color('rosu')
#
# class Triunghi():
#     baza = 0
#     inaltime = 0
#     def __init__(self,baza,inaltime):
#         self.baza = baza
#         self.inaltime = inaltime
#
#     def getArie(self):
#         self.__calculArie()
#         return self.__arie
#
#     def __calculArie(self):
#         self.__arie = self.baza* self.inaltime / 2
# triunghi = Triunghi(7,4)
# print(triunghi.getArie())
#
#
# class CarPy():
#     def __init__(self,color):
#         self.__color = color
#     property
#     def color(self):
#         return self.__color
#     @property
#     def color(self):
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f'Getter: Culoarea este {self.__color}')
#         return self.__color

#     @color.setter
#     def color(self,color):
#         print(f'Setter:Noua culoare este {color}')
#         self.__color = color
#
#     @color.deleter
#     def color(self):
#         print(f'Deleter :Am sters culoarea')
#         self.__color = None
#
# car1 = CarPy('rosu')
# car1.color
# car1.color = 'verde'
# car1.color
# del car1.color
# car1.color
#

