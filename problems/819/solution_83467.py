""" Nesta função, iremos filtrar a lista iterando os itens que satisfazem as 
condições de darem resto 0 para n (ou seja, são divisíveis por n), jogando
esses itens para a nova lista "filtrado".
list, int -> list
"""
def filtraMultiplos(lista, n):
    filtrado = []
    for x in lista:
        if x % n ==0:
            filtrado.append(x)
    return filtrado