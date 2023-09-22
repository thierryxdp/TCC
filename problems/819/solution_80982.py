def filtramultiplos(lista)
"""filtra os multiplos de um numero n"""
lista = [8, 9, -1, -3, 3, -5, -4, 5, -4, 2, 5, 91, -11, 5, 10, 93, -75]
lista_valida = []
for elem in lista:
    if elem > 0:
        lista_valida.append(elem)
print filtramultiplos