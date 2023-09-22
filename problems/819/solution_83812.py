def filtraMultiplos (lista_numeros,num_divisor):
    
    '''
    função que retorna uma lista com numeros filtrados somente divísiveis por n, após receber
    uma lista com números e um numero n para dividir os demais.
    list, int -> list
    '''
    lista_multiplos=[]
    contador=0
    while contador<len(lista_numeros):
        if lista_numeros[contador]%num_divisor==0:
            lista_multiplos= lista_multiplos+[lista_numeros[contador]]
        contador=contador+1
    return lista_multiplos