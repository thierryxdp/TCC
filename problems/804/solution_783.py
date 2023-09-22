def filtra_pares(valor_1,valor_2,valor_3,valor_4):
    lista = [8, 9, -1, -3, 3, -5, -4, 5, -4, 2, 5, 91, -11, 5, 10, 93, -75]
lista_valida = []
for elem in lista:
    if elem %2 ==0 :
        lista_valida.append(elem)
        return lista_valida