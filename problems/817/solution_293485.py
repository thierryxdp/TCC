import math

def acima_da_media(lista):
    '''Retorna uma lista em ordem crescente com as notas que ficaram acima da média
    lista -> lista'''
    primlista = [0,2,4,6,8,10] #lista par
    seglista = [1,3,5,7,9] #lista ímpar
    x = sum(lista)
    a = len(lista)
    b = x/a                  #valor médio
    list.append(lista, b)
    list.sort(lista)
    c = list.index(lista, b)
    d = round(len(lista)/2)      #valor meio da lista ímpar
    e = lista[d] 
    f = lista[c+1:] #lista par
    g = lista[c+2:] #lista ímpar
    if len(lista) in primlista:
        return f
    elif len(lista) not in primlista and b == e:
        return g