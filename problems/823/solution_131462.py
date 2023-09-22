from math import factorial
from math import prod

def faltante(lista):
    ''''recebe lista de numeros. retorna o faltante.'''
    h = 0
    list.sort(lista)
    j = lista[-1] # ultimo da lista ordenada
   # print(prod(lista))
    #print(factorial(j))
    if 1 not in lista:
        return 1
            # 1 CASO - FACIL
    if prod(lista) != factorial(j): #PARA ACHAR ONDE O ERRO ESTA NO `MEIO` DA LISTA
        while h < len(lista):
            if lista[h]+1 != lista[h+1]:
                return lista[h]+1
            h += 1
    else:
        return lista[-1]+1