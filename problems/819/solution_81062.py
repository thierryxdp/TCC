def filtraMultiplos (lista_numeros, n):
    '''funcao que retorna todos os numeros da lista de entrada que
    sao divisiveis pelo numero n dado.
    list(int), int -> list(int)'''
    i=0
    lista= []
    while i<len(lista_numeros):
        if lista_numeros[i]%n ==0:
            lista = lista + lista_numeros[i]
    	i = i+1
        
    return lista