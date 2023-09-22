def faltante (lista):
    a=1
    pecas= [a]
    lista1= len(lista)+1
    while a < lista1:
        pecas += [(a+1),]
        a = a+1
    total_esperado = sum(pecas)
    total_observado = sum(lista)
    return total_esperado - total_observado