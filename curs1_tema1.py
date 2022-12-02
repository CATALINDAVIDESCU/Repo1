#expectedUsername = 'DAVIDESCU CATALIN'
#expectedParola = '1234'
# sold2 = '200'
# print(type(sold2))
# assert type(sold) == type(sold2))
#tema 1
#ex.1 : In cadrul unui comentariu ,explica cu cuvintele tale ce este o variabila.
#variabila = loc din memorie care stocheaza informatii . Ele pot fi de mai multe feluri: intregi , sir de caractere , boolean , float.
#ex2 : Declara si initiaza cate o variabila din fiecare din urmatoarele tipuri:
#string
#int
#float
#universitate = 'Gheorghe Asachi'
# print(type(universitate))
# camine = 22
# print(type(camine))
# pret_camin = 200.35
# print(type(pret_camin))
# admis = True
#print(type(admis))
# #ex 4:Rotunjeste variabila 'float' folosind functia round () si salveaza aceasta modificare in ac variabila (suprascriere),
# #apoi verifica din nou tipul de date al acesteia.
# numar_rotunjit = round(pret_camin)
# print(numar_rotunjit)
# print(type(numar_rotunjit))
#ex5:Foloseste functia print() si printeaza in consola 4 propozitii folosind cele 4 variabile.
# student = True
# print(student)
# print(universitate + ' se afla in Iasi')
# print(f'in campus sunt {camine} de camine')
# print(f'platesc lunar {pret_camin} ron')
#ex.6: Citeste de la tastatura numele si prenumele unei persoane si salveaza - le in cate o variabila
#nume = 'Davidescu'
#nume = input('Numele este :')
#prenume = 'Catalin'
#prenume = input('Prenumele este :')
#print(f'numele complet are {len(nume) + len(prenume)} caractere')
#ex.7: Citeste de la tastatura lungimea si latimea unui dreptunghi si salveaza le in cate o variabila.
# # Afiseaza pe ecran urmatoarea propozitie:Aria dreptunghiului este 'x'.
#lungime = 25
#latime = 15
#print(f'Aria dreptunghiului este {lungime * latime}')
#ex.8: Avand stringul :'Coral is either or the stupidest animal or the smartest rock':
# Afiseaza de cate ori apare cuvantul 'the'.
#string = 'Coral is either or the stupidest animal or the smartest rock'
#string.count('the')
#print(string.count('the'))
# #ex.9
#print(string.replace('the','THE'))

#ex.10
#string =  'Coral is either or the stupidest animal or the smartest rock'
#assert string.isdigit() is True ,'stringul nu contine doar cifre'

#EXERCITII OPTIONALE
#Ex_1 Citeste de la tastatura un string de dimesiune impara si afiseaza caracterul din mijloc.
#text = str(input('Scrie un string:'))
#print(f'Caracterul din mijloc este:{text[len(text)//2]}')

#Ex_2 Folosind assert, verifica daca un string este palindrom.
#text = 'Catalin'
#assert text == text[::-1], 'Cuvantul  nu este palindrom'

#Ex_3 Citeste un string de la tastatura asupra caruia sa efectuezi urmatoarele :
#salveaza fiecare cuvant in cate o variabila;
#printeaza ambele variabile pentru verificare .
# text = str(input('Scrie un string:'))
# a, b = text.split()
# print(f'Primul cuvant este:{a}')
# print(f'Ultimul cuvant este:{b}')

#Ex_4 Citeste un sstring de la tastatura asupra caruia sa efectuezi urmatoarele:
#salveaza primul caracter intr-o variabila;
#capitalizeaza acest caracter peste tot ,mai putin primul si ultimul caracter.
#text = str(input('Scrie un string:'))
#first = text[0]
#x = text[1:(len(text)-1)]
#print(first,x.replace(first,first.upper(),text[len(text)-1]))

#Ex_5 Citeste un user de la tastatura ,citeste o parola .Afisesza :'Parola pt user este **** si are x caractere.
# user = str(input('Userul este:'))
# parola = str(input('Parola este:'))
# parola_ascunsa = '*' * len(parola)
# print(f'Parola pentru userul {user} este{parola_ascunsa} si are {len(parola)} caractere')
