def filtraMultiplos(lista,n):
    '''funcao que filtra os numeros multiplos de um determinado algarismo n''''
    i=0
    resultado=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(resultado, lista[i])
            
        i=i+1
    return resultado