#-------------EXERCICIO 6-------------------

def faltante(lista_pecas):
    '''Retorna peca faltante
        ASSUME pecas numeradas de 1-N
       list -> int'''

    list.sort(lista_pecas)
    i=0       #contador
    
    while i<len(lista_pecas):
        if lista_pecas[i] != i+1:
            return i+1
        i+=1