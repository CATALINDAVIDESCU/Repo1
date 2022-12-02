#exercitiu_1
# class Circle:
#
#     def __init__(self,raza,culoare):
#         self.culoare = culoare
#         self.raza = raza
#     def descriere_cerc(self):
#         return self.raza,self.culoare
#     def aria(self):
#         return 2*PI*self.raza
#     def circumferinta(self):
#         return 2*self.raza
#     def diametru(self):
#         return self.raza**2
# PI = 3.14
# cerc = Circle(12,'verde')
# print(cerc.circumferinta())
# print(cerc.descriere_cerc())
# print(cerc.aria())
# print(cerc.diametru())

#exercitiul_2
# class Right_angle:
#     def __init__(self,lungime,latime,culoare):
#         self.lungime = lungime
#         self.latime  = latime
#         self.culoare = culoare
#     def descrie_dreptunghi(self):
#         return self.lungime,self.latime,self.culoare
#     def aria(self):
#         return self.lungime*self.latime
#     def perimetru(self):
#         return 2*(self.lungime+self.latime)
# dreptunghi = Right_angle(15,8,'albastru')
# print(dreptunghi.descrie_dreptunghi())
# print(dreptunghi.aria())
# print(dreptunghi.perimetru())
#
#
# exercitiul_3
# class Angajat:
#     def __init__(self,nume,prenume,salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     def descrie_angajat(self):
#         return self.nume,self.prenume,self.salariu
#     def nume_complet(self):
#         return self.nume+self.prenume
#     def salariu_lunar(self):
#         return self.salariu
#     def salariu_anual(self):
#         return self.salariu*12
#     def marire_salariu(self):
#         return (procent/100)*self.salariu
# procent = 12
# salariat = Angajat('Davidescu','Catalin',7000)
# print(salariat.descrie_angajat())
# print(salariat.nume_complet())
# print(salariat.salariu_lunar())
# print(salariat.salariu_anual())
# print(salariat.marire_salariu())
#
# exercitiul_4
#
#class Cont:
     # def __init__(self,iban,titular_cont,sold):
     #     self.iban = iban
     #     self.titular_cont = titular_cont
     #     self.sold = sold
     #
     # def afisare_sold(self):
     #     print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
     # def debitare_cont(self,suma):
     #     if suma >= self.sold:
     #         self.sold-= suma
     #     else:
     #         print('Fonduri insuficiente')
     # def creditare_cont(self,suma):
     #     self.sold += suma


#Exercitii optionale
# #Clasa factura. Atribute: seria(va fi constanta ,nu trebuie constructor,toate facturile vor avea aceasi serie )
# # numar,nume_produs,cantitate,pret_buc
# #  Constructor : toate atributele ,fara serie
# # Metode :schimba_cantitea (cantitate), schimba_pretul(pret), schimba_nume_produs(nume),genereaza _factura().
# #from datetime import date
# #from tabulate import tabulate
# class Factura:
#     seria ='AC'
#     numar = 0
#     nume_produs = None
#     cantitate = 0
#     pret_buc = 0
#     def __init__(self,numar, nume_produs,cantitate,pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc  = pret_buc
#     def schimba_cantitatea(self,cantitate_noua):
#         self.cantitate = cantitate_noua
#     def schimba_pretul(self,pret):
#         self.pret_buc = pret
#     def schimba_nume_produs(self,nume):
#         self.nume_produs = nume
#     def genereaza_factura(self):
#         print(f'Factura seria: {self.seria} numar:{self.numar}')
#         dataora = datetime.now()
#         data_azi = dataora.date()
#         print(f'Data: {data_azi}')
#         print('Produs  |  Cantitate  |  Pret bucata | Total  |')
#         print(f' {self.nume_produs}  |
#         {self.cantitate}  |  {self.pret_buc}  |  {self.cantitate* self.pret_buc}  |')


# class Masina:
#     marca = 'Dacia'
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = ['rosu','verde','alb','albastru','portocaliu','negru','galben']
#     inmatriculata = False
#     def __init__(self,model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descriere(self):
#         print(f'Marca masinii este :{self.marca}')
#         print(f'Modelul masinii este:{self.model}')
#         print(f'Viteza masinii este:{self.viteza_maxima}')
#         print(f'Viteza actuala a masinii este :{self.viteza_actuala}')
#         print(f'Culoarea masinii este :{self.culoare}')
#         print(f'Masina este inmatriculata:{self.inmatriculata}')
#
#     def inmatrriculare(self):
#         self.inmatriculata = True
#         return self.inmatriculata
#     def vopseste_masina(self,noua_culoare):
#         if noua_culoare in self.culori_disponibile:
#             self.culoare = noua_culoare
#             print(f'Noua culoare este:{self.culoare}')
#         else:
#             print('Culoarea aleasa de dumneavoastra nu este in paletarul nostru.')
#
#     def accelereaza(self,viteza_dorita):
#         if viteza_dorita < 0:
#             print('Eroare!')
#         elif viteza_dorita >= self.viteza_maxima :
#             self.viteza_actuala = self.viteza_maxima
#         else:
#             self.viteza_actuala = viteza_dorita
#             print(f'Viteza actuala este :{self.viteza_actuala}')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#         print(f'Viteza actuala este :{self.viteza_actuala}.Am oprit masina!')
