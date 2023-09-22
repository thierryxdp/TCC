def filtraMultiplos(lista, n):
    '''Recebe uma lista de numeros e um numero e retorna outra lista
    contendo todos os elementos da lista original que forem divisiveis por n;
    list,int -> list'''
    contador = 0
    numeros=[]
    while contador<len(lista):
        if lista[contador]%n==0:
            numeros = numeros + list(lista[contador])
        contador=contador+1
    return numeros