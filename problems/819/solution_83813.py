def filtraMultiplos(lista_numeros,n):
    '''
       Dada uma lista de números e um número n a função 
       retorna uma nova lista apenas com os números que 
       são divisíveis por n.
       list,int -> list
    '''
    i=0
    multiplos=[]
    while i<len(lista_numeros):
        if lista_numeros[i]%n==0:
            list.append(multiplos,lista_numeros[i])
        i = i + 1
    return multiplos