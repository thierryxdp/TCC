def faltante(lista_inteiros):
    '''crie uma função que, dada uma lista de números inteiros numerados de 1 a N, retorne o número inteiro desde intervalo que está faltando. list-->int.'''
    indice = 1
    if lista_inteiros[0] != 1:
        return 1
    if lista_inteiros[0] == 1 and len(lista_inteiros)==1:
        return 2
    while indice<len(lista_inteiros):    
        if lista_inteiros[indice]-(lista_inteiros[indice-1])==2:
            return lista_inteiros[indice]-1   
        elif len(lista_inteiros) == lista_inteiros[-1]:
            return lista_inteiros[-1]+1
        indice = indice+1