def repetidos(lista):
    """função que recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior;list-->int"""
    NumVezes=0
    i=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            NumVezes+=1
        i+=1
    return NumVezes