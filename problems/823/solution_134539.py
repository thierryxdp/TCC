def faltante (lista):
    '''dada uma lista com N-1 inteiros numerados de 1 a N, retorna o número da ordem que está faltando'''
    '''lista->int'''
    a=1
    pecas= [a]
    lista1= len(lista)+1
    while a < lista1:
        pecas += [(a+1),]
        a = a+1
    total_esperado = sum(pecas)
    total_observado = sum(lista)
    return total_esperado - total_observado