def repetidos(lista):
    '''funçao que recebe uma lista de numeros e retorna o numero de vezes
    que ocorre uma repetição de um elemento seguido do outro
    entrada: list
    saida: int'''
    i=0
    contagem=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            contagem=contagem+1
        i=i+1
    return contagem