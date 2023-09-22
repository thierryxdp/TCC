def filtraMultiplos(lista,n):
    '''
    funcao que recebe de entrada uma lista de
    numeros e um numero n e retorna outra lista
    com todos os elementos da primeira que sao
    divisiveis pelo numero n
    list,int->list
    '''
    y=[]
    x=0
    while x<len(lista):
        if lista[x]%n==0:
            y.append(lista[x])
        x=x+1

    return y