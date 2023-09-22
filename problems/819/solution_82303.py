def filtraMultiplos(listadenumeros:list, n:int):
    '''Recebe uma lista de números e um número(n) e retorna
    uma outra lista com todos os números originais que forem
    divisíveis por n'''
    i=0
    lista=[]
    #verifica se o I é menor que a lista de entrada
    while i <len(listadenumeros):
        #verifica se os números são múltiplos
        if listadenumeros[i]%n==0:
            #Sendo múltiplo, adiciona o número na lista nova
            lista.append(listadenumeros[i])
        #Acrescenta 1 ao I
        i+=1
        return lista