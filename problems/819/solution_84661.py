'''
list, int -> list

Função que recebe uma lista e um número n e retorna uma 
outra lista com os números da primeira lista que são divisíveis 
por n
'''
def filtraMultiplos(lista, n):
    contador = 0
    divisiveis = []
    while contador<len(lista):
        if lista[contador]%n==0:
            divisiveis = divisiveis + [lista[contador]]
        contador = contador + 1
    return divisiveis