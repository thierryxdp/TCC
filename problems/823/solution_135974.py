def maxlista(lista):
    maior = max(lista)
    n = 0
    lista1 = [maior]
    
    while n < max(lista):
        lista1 = lista1 + [ maior - 1 ]
        maior = maior - 1
        n = n + 1
        

    return lista1

def faltante(listanum):

    
    if sum(listanum) == sum(maxlista(listanum)):
        return max(listanum) + 1

    elif sum(listanum) != sum(masxlista(listanum)):
        return sum(maxlista(listanum)) - sum(listanum)