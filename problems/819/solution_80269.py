def filtraMultiplos(lista,n):
    """recebe uma lista de numeros e um numero e retorna outra contendo os elementos divisiveis por n"""
    contador = 0
    saida= []
    while contador<len(lista):
        if lista[contador]%n == 0:
            saida +=[lista[contador]]
            contador+=1
        else:
            contador+=1
    return saida