# optiune = int(input('alege optiunea '))
# if optiune ==0:
#     print('meniul anterior')
# elif optiune == 1 :
#     print('ati ales ro')
# elif optiune == 2:
#     print('ati ales eg')
# else:
#     print('mai incearca')

# pentru un bancomat verificam userul si parola. userul are doar 2 incercari atat pt username cat si pt parola
# userul dorese sa scoata o anumita suma de bani acesta avand un sold curent.
# Suma dorita trebuie sa fie mai mica decat soldul curent.daca suma este prea mare poate sa aleaga daca dorestye sa reincerce sau nu
# la a 2 a incercare daca userul introduce o suma mai mare iese din program
# expectedUser = 'ION'
# expectedPass = '1234'
# sold = 50000
# username = input('introduceti username :')
# if username == expectedUser:
#     print('user corect')
# else:
#     print('username incorect')
#     username = input('introduceti username :')
#     print('user corect')
#     assert username == expectedUser,'usrname incorect .o zi frumoasa!'
#     print('user incorect')
# parola = input('introduceti parola :')
# if parola == expectedPass:
#     print('parola corecta')
# else:
#     print('parola incorecta , incercati din nou')
#     parola == input('introduceti parola')
#     assert parola == expectedPass, 'parola incorecta'
#     print('parola corecta')
# suma = float(input('introdu suma dorita:'))
# if suma <= sold:
#     print('ridicati banii')
# else:
#     print('suma dorita este prea mare .fonduri insuficiente')
#     reincercare = input('doriti sa reincercati? da / nu:')
#     if reincercare == 'da':
#         suma = float(input('introdu suma dorita'))
#         assert suma <= sold ,'suma introdusa = prea mare'
#         print('RIDICATI BANII')
#     elif reincercare =='nu':
#         print('la revedere')
#     else:
#         assert False,'eroare'


# JOC DE NOROC CU ZAR
# import random
# zar =[1,2,3,4,5,6]
# diceroll = random.choice(zar)
# numarAles = int(input('alege un numar'))
# if numarAles < diceroll:
#     print(f'ai pierdut ai ales un numar mai mic.ai ales {numarAles},dar a fost {diceroll}')
# elif numarAles > diceroll:
#     print(f'ai pierdut ai ales un numar mai mare . ai ales numarul {numarAles} dar a fost {diceroll}')
# else:
#     print('ai castigat')

# ex 1: explica cu cuvintele tale intr un comentariu cum functioneaza un if else
# daca conditie  = True se executa bloc de cod
# altfel se executa acest bloc de cod

# ex.2 verifica si afiseaza daca x este numar natural sau nu ( un numar se considera natural daca
# este numar intreg mai mare ca 0)
# x = 7
# if x >= 0 and type(x == int):
#     print(f'{x} este numar natural')
# else:
#     print(f'{x} nu este numar natural')

# ex.3 verifica si afiseaza daca x este numar pozitiv ,negativ sau neutru
# x = 8
# if x > 0:
#     print(f' este numar pozitiv')
# elif x < 0:
#     print(f' este numar negativ')
# else:
#     print(' este numar neutru')

# ex.4 verifica si afiseaza daca x este intre -2 si 13 incluzand capetele de interval
# x = 9
# if x > -2 and x < 13:
#     print(f'numarul {x} se afla in intervalul -2 , 13')
# else:
#     print(f'numarul {x} nu se afla in acest interval')

# ex.5verifica daca diferenta dintre x si y este mai mica de 5
# x = 14
# y = 9
# if x - y < 5:
#     print('diferenta este mai mica decat 5')
# else:
#     print('diferenta este mai mare decat 5')

# ex.6 verifica daca x nu este intre 5 si 27 incluzand capetele de interval.
# x = 2
# if not (5 <=x <= 27):
#     print(f'numarul  nu este intre 5 si 27')


# ex.7 declara o noua variabila y de tip int apoi verifica si afiseaza daca x si y sunt egale ,
# daca nu afiseaza care din ele e mai mare
# x= 7
# y = 7
# if x == y:
#     print('numerele x si y sunt egale')
# elif x > y:
#     print(f'{x} este valoarea lui x si este mai mare decat y')
# else:
#     print(f'{y} este valoare lui y si este mai mare decat x')

# ex.8 presupunand ca x,y,z (toate tip int) reprezinta laturile unui triunghi
# x = 4
# y = 4
# z = 4
# if (x == y and x!= z) or (x == z and x != y) or (y == z and y != x):
#     print('triunghiul este isoscel')
# elif x == y == z :
#     print('triunghiul este echilatral')
# else:
#     print('triunghiul este oarecare')

# ex.9 citeste o litera de la tastatura apoi verifica si afiseaza daca este o vocala sau nu
# letter = input('introduceti o litera:')
# letter = letter.lower()
# if letter.isdigit():
#     print('nu ai introdus o litera ci altceva')
# elif letter.upper() == 'A' or letter.upper() == 'E'or letter.upper() == 'I'or letter.upper() == 'O'or letter.upper() =='U':
#     print('litera este vocala')
# else:
#     print('litera nu este vocala')

# EX 10 transforma si printeaza notele din sistem romanesc in sistem american dupa cum urmeaza:
# peste 9 =>A
# peste 8 => B
# peste 7 => C
# peste 6 => D
# peste 4 => E
# 4 sau sub => F
# nota = float(input('care este nota primita?'))
# if 9 < nota <= 10:
#     nota = 'A'
#     print(f'nota primita in sistemul american este {nota}')
# elif nota >= 8:
#     nota = 'B'
#     print(f'nota in sitemul american este {nota}')
# elif nota >= 7:
#     nota = 'C'
#     print(f'nota in sistemul american este{nota}')
# elif nota >= 6:
#     nota = 'D'
#     print(f'nota in sistemul american este {nota}')
#
# elif nota > 4:
#     nota = 'E'
#     print(f'nota primita in sistemul american este {nota}')
# elif 4 >= nota >= 0:
#     nota = 'F'
#     print(f'nota in sistemul american este {nota}')
#
# else:
#     print('nu a ti introdus nici o nota de la 0 la 10')

# EXERCITII OPTIONALE
# EX_1 Verifica daca x are minim 4 cifre (ex:3456 are 4 cifre ,10 nu are minim 4 cifre )
# x = int(input('Introduceti numarul:'))
# y = len(str(x))
# if y >= 4:
#     print('numarul are 4 cife')
# else:
#     print('numarul nu are 4 cifre')

# EX_2 Verifica daca x are exact 6 cifre .
# x = int(input('introduceti un numar :'))
# y = len(str(x))
# if y == 6:
#     print('numarul are 6 cifre')
# else:
#     print('numarul nu are 6 cifre')

# Ex_3 Verifica daca x este numar par sau impar ( x e int).
# x = int(input('Scrie un numar:'))
# if x% 2==0:
#     print('numarul este par')
# else:
#     print('numarul este impar')

# EX_4 x,y,z (int)
# Afiseaza care este mai mare dintre ele.
# x = int(input('Primul numar este:'))
# y = int(input('Al doilea numar este:'))
# z = int(input('Al treilea numar este :'))
# if x>y and x >z:
#     print(f'{x } este cel mai mare numar')
# elif y>x and y>z:
#     print(f'{y} este cel mai mare numar ')
# elif z>x and z>y:
#     print(f'{z} este cel mai mare numar ')
# else:
#     print('Minim 2 numere sunt egale')

# Ex_5 x,y,z reprezinta unghiurile unui triunghi.
# verifica si afiseasza daca triunghiul este valid sau nu.
# x = 90
# y = 60
# z = 30
# if x+y+z == 180 and x>0 and y>0 and z>0:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')

# Ex_6 Avand stringul : 'Coral is either the stupidest animal or the smartest rock' citeste de la tastatura un numar x de tip int
# si afiseaza stringul fara ultimele x caractere .
# string = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Alege catre caractere vrei sa tai la final:'))
# print(string[0:-x])

# Ex_7 Avand ac string de la ex 6 ,declara un string nou care sa fie format din primele si ultimele 5 caractere
# string = 'Coral is either the stupidest animal or the smartest rock'
# string1 = string[0:5]
# string2 = string[-5:]
# print(f'{string1}{string2}')

# Ex_8 Ac string ca la 7 ,salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# Folosind ac variabila + slicing afiseaza tot stringul pana la acest cuvant
# Output asteptat: 'Coral is either the stupidest animal or the smartest'
# string = 'Coral is either the stupidest animal or the smartest rock'
# x = 'rock'
# index = string.find(x)
# print(string[0:index])

#Ex_9 Citeste de la tastatura un string .
#Verifica daca primul si ultimul caracter sunt la fel.Se va folosi un assert .
#Atentie: se doreste ca programul sa fie case insensitive -'apA'- e acceptat.
# string = input('Scrieti un cuvant:')
# assert string[0].lower()== string[len(string)-1].lower(),'Primul si ultimul caracter NU sunt la fel'
# print('Primul si ultimul nu sunt la fel')

#EX_10 Avand stringul '0123456789'
#Afisati doar numerele pare
#Afisati doar numerele impare
# string = '0123456789'
# print('Pare:'+ string[0:len(string):2])
# print('Impare:'+string[1:len(string):2])


