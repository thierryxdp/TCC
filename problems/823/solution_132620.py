def faltante(lista):
    '''Função que recebe uma lista com N-1 inteiros numerados de 1 a N e
    retorna qual número inteiro do intervalo está faltando.
    
    lista -> int'''
    
    lista.sort
    i = 0
    
    if lista[0] == 1:
        while i<len(lista):
            if lista[i]+1 != lista[i+1]:
                return lista[i]+1
            i=i+1
        return lista[-1]+1