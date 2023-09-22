def filtraMultiplos(numeros,n):
    '''Esta e a funcao que dado uma lista e um numero n, 
    filtra os multiplos deste numero n na lista. 
    retornando uma lista com os numeros que sao multiplos 
    de n.'''
    j=0
    numeros2=[]
    while j<len(numeros):
        if numeros[j]%n==0:
            numeros2.append(numeros[j])
        j=j+1
    return numeros2