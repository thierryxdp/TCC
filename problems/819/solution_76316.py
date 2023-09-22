'''
Recebe uma lista e um inteiro, retorna os elementos da lista que o inteiro divide.
list, int -> list
'''
def filtraMultiplos(lista, n):
    nova = []
    for item in lista:
        if item%n==0:
            nova.append(item)
    return nova