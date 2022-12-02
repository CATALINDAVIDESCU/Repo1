import random  # def print_hi():
#     print('Hello Wordlds')
#     print('Hello 2')
# print_hi()
#
# def print_hi(user,age = 3):
#     print(age)
#     print(f'hi{user}')
# print_hi ('Catalin',42)
# def is_natural(numar):
#     if numar >= 0:
#         return True
#     else:
#         return False
#
# if is_natural(4):
#     print('numarul este natural')
# else:
#     print('numarul nu est este natural')
#
# def contBancar (username, parola, plata):
#     i = 0
#     while i < 3:
#         if username == 'DAVIDESCU CATALIN':
#             if parola == '1234':
#                 if plata <='200':
#                     print('Tranzactie reusita!')
#                     break
#                 else:
#                     print('fonduri insuficiente!')
#                     break
#             else:
#                 print('Parola gresita!')
#                 Parola =input('Parola:')
#                 i+=1
#         else:
#             print('Username gresit!')
#             username = input('ID:')
#             i+=1
#     print(f'Multumim.O zi frumoasa!')
# contBancar(input('ID:'),input('Parola:'),input('Sold:'))
#
# expectedUsername = 'DAVIDESCU CATALIN'
# expectedParola = '1234'
# sold = 200
# #
# def bubblesort (lista):
#      for i in range(len(lista)-1):
#         for j in range(len(lista)-1):
#             if lista[j] > lista[j+1]:
#                 lista[j] , lista[j +1] = lista[j +1 ],lista[j]
#      return lista
# #
# # lista_sortata = bubblesort([3,6,8,1,4,9,0,10])
# # print(lista_sortata)
#
# def lista_max(lista):
#     lista_sortata = bubblesort(lista)
#     return lista_sortata[-1]
# maxim = lista_max([3,6,8,1,4,9,0,10])
# print(maxim)
# def list_max2(lista):
#     maxim = 0
#     for i in range(len(lista)):
#         if max < lista[i]:
#             maxim = lista[i]
#     return maxim
#     zar = [1,2,3,4,5,6]
#     numar_zar = random.choice(zar)
#     numarAles = int(input('alege un numar'))
#     if numarAles < numar_zar:
#         print(f'ai pierdut ai ales un numar mai mic.ai ales {numarAles},dar a fost {diceroll}')
#     elif numarAles > numar_zar:
#         print(f'ai pierdut ai ales un numar mai mare . ai ales numarul {numarAles} dar a fost {diceroll}')
#     else:
#         print('ai castigat')
# def diceroll():


#TEMA 5

##ex1.
#numar1 = 18
#numar2 = 10
#total = numar1 + numar2
#print(total)
#def numere(x ,y):
    #return(x + y)
##print(numere(18,10))
#def numere2(a,b):
   # return (a + b)
#print(numere2(22,18))

#ex.2Functie care ssa returneze TRUE daca un numar este par sau FALSE daca este impar
# def par_impar(numar):
#     if numar % 2 ==0:
#         return True
#     else:
#         return False
# print(par_impar(67))
# print(par_impar(30))
# #ex.3
#def numele_meu(nume,prenume):
    #return (len(numele_meu()))
#print(len('Davidescu Catalin'))
#print(len('Elena Davidescu'))

# #ex4.
# def dreptunghi(lungime, latime):
#     return(lungime*latime)
# print(f'Aria dreptunghiului este :{dreptunghi(15,10)}')
# print(f'Aria dreptunghiului este :{dreptunghi(30,10)}')

#ex.5
# def cerc(pi, raza):
#     return(pi*(raza**2))
# print(f'ARIA CERCULUI ESTE :{cerc(3.14 , 12)}')

#ex.6
# string = input('string:')
# chr = input('Caracter cautat:')
# def caracter_2(x):
#         if x in string:
#             return True
#         else:
#             return False
# print(caracter_2('laptop'))

#ex.7
# felicitare = input('Va urez:')
# def revelion(s):
#     x = {'upper_case':0, 'lower_case':0}
#     for i in s :
#         if i.isupper():
#             x['upper_case']+=1
#         if i.islower():
#             x['lower_case']+=1
#     print(f"Nr caractere mici :{x['lower_case']}")
#     print(f"Nr caractere mari: {x['upper_case']}")
# print(revelion(felicitare))

#ex8.
# lista_numere = [-5,7,2,9,12,3,1,-6,-4,3]
# def numere_pozitive(numere):
#     lista_numere_pozitive = []
#     for numar in numere:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return lista_numere_pozitive
# print(numere_pozitive(lista_numere))


#ex9
# def numere(x,y):
#     if x == y:
#         print(f'numerele sunt egale')
#     elif x > y:
#         print(f'numarul  {x} este mai mare decat numarul {y}')
#     else:
#         print(f'numarul {y} este mai mare decat numarul {x}')
# numere(34,45)


# #ex.10
# def zi_nastere(numar,set):
#     if numar in set:
#         print(f'Nu am adaugat numarul {numar} in set .Acesta exista deja!')
#         return True
#     else:
#         print(f'Am adaugat numarul {numar} in set')
#         return False
# zi_nastere(6,{0,3,0,6})
#
#ex 1bonus
# list1 = [3,4,5,6,7,8]
# list2 = [2,1,5,3,8,9]
# def lista_numere(l1,l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     s3 = s1 & s2
#     return list(s3)
# print(lista_numere(list1,list2))

#Exercitii_Optionale
#Functie care primeste o luna din an si returneaza cate zile are.
# def calendar(luna):
#     lunile_anului={
#         'Ianuarie':31,
#         'Februarie':28,
#         'Martie':31,
#         'Aprilie':30,
#         'Mai':31,
#         'Iunie':30,
#         'Iulie':31,
#         'August':31,
#         'Septembrie':30,
#         'Octombrie':31,
#         'Noeiembrie':30,
#         'Decembrie':31}
#     if luna in lunile_anului:
#         return lunile_anului.get(luna)
# print(calendar('Decembrie'))

#EX2 Functie calculator care sa returneze 4 valori:suma ,diferenta,inmultirea , impartirea a 2 numere
# def calculator(x,y):
#     a = x+y
#     b = x-y
#     c = x*y
#     d = x/y
#     return a,b,c,d
# a,b,c,d = calculator(8,2)
# print(a)
# print(b)
# print(c)
# print(d)

#Ex3 Functie care primeste 3 numere .Returneaza valoarea maxima dintre ele.
# def maxim(x,y,z):
#     if x==y and y == z:
#         max = x
#     elif x >=y and x >= z:
#         max = x
#     elif y >=x  and y >= z:
#         max = y
#     else:
#         max = z
#     return max
# print(max(8,5,3))
# print(max(4,3,2))

#Ex4Functie care sa primeasca un numar si sa returneze suma uturor numerelor de la 0 la ac numar.
# def suma_nr(a):
#     suma = 0
#     for i in range(0,a + 1):
#         suma = suma + i
#     return suma
# print(suma_nr(9))

# #EX5Functie care primeste 2 liste de numere .Returnati numerele comune.
# list1 =[2,3,4,4,5,3,]
# list2 =[4,5,6,2,7,8]
# def common_nr(l1,l2):
#     set1=set(l1)
#     set2 =set(l2)
#     return set1.intersection(set2)
# print(common_nr(list1,list2))

