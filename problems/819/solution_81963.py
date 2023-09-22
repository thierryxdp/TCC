def filtraMultiplos(lista_numeros,numero):
    ''' Essa função recebe uma lista de números e um número e retorna uma outra lista contendo todos os elementos originais que forem
    divisíveis pelo número.
    list,int->list
    '''
    contador=0  
    lista_nova=[]
    while contador<len(lista_numeros):
        if lista_numeros[contador]%numero==0:
            lista_nova.append(lista_numeros[contador])
        contador=contador+1
    
    return lista_nova