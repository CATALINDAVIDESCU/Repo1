# from abc import ABC ,abstractmethod
# #ABSTRACTION
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#     @abstractmethod
#     def aria(self):
#         pass
#     @classmethod
#     def descrie(cls):
#         print('cel mai  probabil am colturi')
#
# #INTHERANCE
#
# class Patrat(FormaGeometrica):
#     def __init__(self,latura):
#         self.__latura = latura
#     def aria(self):
#         return self.__latura*self.__latura
# #Property
#     @property
#     def latura(self):
#         return self.__latura
#     @latura.getter
#     def color(self):
#         print(f'Getter:latura este{self.__latura}')
#         return self.__latura
#     @latura.setter
#     def color(self,latura):
#         print(f'Setter: Noua latura este {latura}')
#         self.__latura = latura
#
#     @latura.deleter
#     def color(self):
#         print(f'Deleter :Am sters latura')
#         self.__latura = None
#
# class Cerc(FormaGeometrica):
#     def __init__(self,raza):
#         self.__raza = raza
#     @property
#     def raza(self):
#         return  self.__raza
#     @raza.getter
#     def raza(self):
#         print(f'Raza cercului este : {self.__raza}')
#         return self.__raza
#     @raza.setter
#     def raza(self,raza):
#         print(f'Noua valoare a razei este :{raza}')
#         self.__raza = raza
#     @raza.deleter
#     def raza(self):
#         print(f'Am sters valoarea razei')
#         self.__raza = 0
#     def aria(self):
#         aria_cercului =self.PI*self.__raza**2
#         return  aria_cercului
#     def descrie(self):
#         print('Eu nu am colturi')
#
#
