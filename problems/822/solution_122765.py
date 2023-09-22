def repetidos(lista):
    """recebe uma lista e retorna o numero de vezes que um elemento da lista é igual ao anterior . List--> int"""
    count = 0
    soma = 0
    while count < len(lista):
        if count == 0:
            count+=1
        else:
            if lista[count] == lista[count-1]:
                soma += 1
            count+=1
    return soma