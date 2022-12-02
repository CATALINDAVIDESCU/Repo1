# masini = ['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
# for i in range(len(masini)):
#     print(f'FOR:Masina mea prefera este : {masini[i]}')
# for masina in masini:
#     print(f'FOR EACH :Masina mea preferata este:{masina}')
#
# i = 0
# while i < len(masini):
#     print(f'WHILE:Masina mea preferata este:{masina}')
#     i = i + 1
#
#
#
# # #ex 2
# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
# else:
    #print(masini)
# #ex 3
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#for masina in masini:
    #if masina == 'Mercedes':
        #print('Am gasit masina cautata de dumneavostra {Mercedes}')
        #break
    #else:
        #print(f'Am gasit masina {masina}.mai cautam')

# #ex 4
#for masina in masini:
    #if masina == 'Trabant' or masina == 'Lastun':
        #continue
    #print(f'S-ar putea sa va placa masina:{ masina}')
# #ex 5 Modernizeaza parcul de masini:
#Creaza o lista goala ,masini_vechi
 #itereaza prin masini
 #cand gasesti Lastun sau Trabant :
     #salveaza aceste masini in masini_vechi
     #suprascriele cu 'Tesla' in lista initiala de masini
 #printeaza modelele vechi,modelele noi
# masini_vechi = []
# items_to_move = ['Trabant','Lastun']
# for index ,item in list(enumerate(masini)):
#     if item in items_to_move:
#         masini.remove(item)
#         masini_vechi.append(item)
#         masini.append('Tesla')
#         print(f'VECHI:{masini_vechi}')
        #print(f'NOI :{masini}')
# #ex6Avand dict :
#pret_masini = {'Dacia': 6800,
               #'Lastun':500,
               #'Opel':1100,
               #'#Audi':19000,
               #'BMW':23000}
#buget = 15000
##or masina, pret in pret_masini.items():
    #if pret <= buget:
        #print(f'va putem oferii masina:{masina}')
# #ex7 Avand lista :
#numere = [5,7,3,9,3,1,0,-4,3]
#for i in numere:
    #print(i)
#ele = 3
#x = [i for i in numere if i == ele]
#print("numarul",ele, "se repeta de",len(x),"ori")
# #ex 8
#numere =[5,7,3,9,3,3,1,0,-4,3]
#suma = 0
#for numar in numere:
    #suma = suma + numar
    #print(f'suma numerelor din lista este:{suma}')
#ex9
#max = numere[0]
#for numar in numere:
    #if numar > max:
       # max = numar
#print(f'cel mai mare numar din lista este: {max}')
# # ex 10
#numere_negative =[-x  for x in numere]
# print(numere_negative)
# #sau
# lista_neg = []
# for numar in numere:
#     if numar > 0:
#         numar = numar-numar*2
#         numar = -(abs(numar))
#     lista_neg.append(numar)
# print(f'lista a devenit: {lista_neg}')


#EXERCITII_OPTIONALE
#1
# alte_numere = [-5,7,2,9,12,3,1,-6,-4,3]
# numere_pare =[]
# numere_impare = []
# numere_pozitive =[]
# numere_negative = []
# for numar in alte_numere:
#     if numar % 2 ==0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar > 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
# print(f'Lista cu numere pare este:{numere_pare}')
# print(f'Lista cu numere impare este:{numere_impare}')
# print(f'Lista cu  umere pozitive este:{numere_pozitive}')
# print(f'Lista cu numere negative este:{numere_negative}')

#Ex2 Aceeasi lista :
#Ordoneaza crescator lista fara sa folosesti sort.
# alte_numere = [-5,7,2,9,12,3,1,-6,-4,3]
# for i in range(len(alte_numere)):
#     for j in range(len(alte_numere)):
#         if alte_numere[i] < alte_numere[j]:
#             alte_numere[i],alte_numere[j]= alte_numere[j],alte_numere[i]
# print(alte_numere)

#Ex3
#Ghicitoare de numar:
#numar_secret = generati un numar random intre 1 si 30
# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = None
# while numar_ghicit is None:
#     nr = int(input('Introdu un numar:'))
#     if nr > numar_secret:
#         print('Numarul secret este mai mic')
#     elif nr < numar_secret:
#         print('Numarul sectret este mai mare')
#     else:
#         print('Felicitari ai ghicit numarul')
#         break

#Ex4
#Alege un numar de la tastatura.
# scrie un program care sa genereze in consola urmatoarea piramida
# nr = int(input('Scrie un numar:'))
# i = 1
# while i <= nr:
#     print('')
#     for j in range(i):
#         j = i
#         print(j,end ='')
#         j = j + 1
#     i = i + 1

#Ex5
# tastatura_telefon =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]]
# for row in tastatura_telefon:
#     for column in row:
#         print(f'FOR EACH :cifra curenta este :{column}')