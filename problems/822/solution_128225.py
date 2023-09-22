def repetidos (lista):
    '''essa funçao recebe uma lista de numeros e retorna quantas vezes um elemento é igual ao anterior
lista -> int'''
    i=1
    a=0
    while i < len(lista):
        if lista[i]==lista[i-1]:
            a=a+1
        i=i+1
    return a