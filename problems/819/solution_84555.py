def filtraMultiplos(lista,n):
    '''Função que retorna uma lista contendo todos os
    elementos da lista de entrada que são divisíveis pelo
    número n. list,int -> list'''
    
    numeros=[]
    proximo=0
    
    while proximo<len(lista):
        if lista[proximo]%n=0:
            numeros=numeros+[lista[proximo]]
        proximo=proximo+1                                                                                                                                                                       
    return numeros