def faltante(pecas):
    '''Função que identifica qual numero da peça que está faltando dada 
    uma lista de numeros como entrada.
    lista -> int'''
    
    lista = []
    indice = 0
    
    while indice < (len(lista)-1):
        if pecas[indice] > pecas[indice+1]:
        lista.append(indice)
        indice =+ 1
    return lista