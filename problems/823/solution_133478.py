def faltante(lista):
    '''Função que verifica qual a peça que esta faltando de uma lista
list -> int'''
    i = 1
    while i < len(lista):
        if  lista[i] - lista[i - 1] > 1:
            return lista[i]-1
    i = i+1