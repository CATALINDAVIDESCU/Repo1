#ex 1
# note_muzicale = ['do','re','mi','fa','sol','la','si','do']
# print(note_muzicale)
# note_muzicale=note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
# #ex 2 printeaza de cate ori apare 'do'.
# print(note_muzicale.count('do'))

# #ex.3 Avand doua liste ,[3,1,0,2] si [6,5,4] gaseste 2 variante sa le unesti intr-o singura lista.
# lista1 = [3,1,0,2]
# lista2 = [6,5,4]
# lista3 = lista1 + lista2
# print(lista3)
# lista1.extend(lista2)
# print(lista1)
# #ex 4 sorteaza si afiseaza lista generata anterior .sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
# lista1.pop(2)
# print(lista1)
# #EX.5 folosind un if verifica lista generata la ex 3 si afiseaza pe fiecare ramura urmatoarele :
# if len(lista3)>= 1:
#     print('lista nu este goala')
# else:
#     print('lista este goala')
# #
# # #ex.6 Foloseste o functie care sa goleasca lista de la ex 3.
# lista3.clear()
# print(lista3)
# # #ex.7 Rescrie if ul de la ex 5 si verifica inca o data rezultatul. Acum ar trebuii sa afiseze ca lista este goala
# if len(lista3)>= 1:
#     print(lista3)
# else:
#     print('lista este goala')
#EX.8 Avand dictionarul = {'Ana':8, 'Gigel':10,'Dorel':5} ,foloseste o functie ca sa afisezi elevii(cheile).
#dict1 = {'Ana':8,'Gigel':10,'Dorel':5,}
#print(dict1.keys())
#ex.9 Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor.
# print(f'Ana a luat nota:{dict1["Ana"]}')
# print(f'Gigel a luat nota:{dict1["Gigel"]}')
# print(f'Dorel a luat nota:{dict1.get("Dorel")}')
# #ex 10 imagineaza ti ca Dorel a facut contestatie si a primit nota 6
# dict1['Dorel']= 6
# print(dict1)
# #ex11
# dict1.__delitem__('Dorel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

#ex 12 Ai urmatoarele seturi :
#zilele_saptamanii ={'luni','marti','miercuri','joi','vineri','sambata','duminica'}
#weekend = {'sambata','duminica'}
#zilele_saptamanii.add('luni')
#print(zilele_saptamanii)
#ex13 foloseste un if si verifica daca weekend este un subset al zilelor din saptamana
#weekend nu este un subset al zilelor si saptamana
#else:
    #print('weekend nu este un subset al zilelor sapatamanii')
#ex 14 Afiseaza diferentele dintre aceste 2 seturi adica elementele care sunt in zilele_saptamanii si nu sunt in weekend si invers
#diferenta1 = zilele_saptamanii.difference(weekend)
#diferenta2 = weekend.difference(zilele_saptamanii)
#print(f'diferenta dintre zilele_saptamanii si weekend este :{diferenta1}')
#ex.15 Afiseaza intersectia elementelor din ac 2 seturi:
#intersectia = zilele_saptamanii.intersection(weekend)
#print(intersectia)

