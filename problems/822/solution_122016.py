def repetidos(lista):
    '''funcao que retorna a quantidade de numeros repetidos dentro de uma lista
    list->int'''
    soma=0
    i=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            soma=soma+1
        i=i+1
    return soma