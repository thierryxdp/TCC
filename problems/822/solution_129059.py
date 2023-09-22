def repetidos(lista):
    '''funcao que recebe uma lista de numeros e retorna o numero de vezes que
    um elemento da lista é igual ao anterior'''
    i=1
    result=0
    while i<len(lista):
        if lista[1]==lista[(i-1)]:
            result=result + 1
        i=i+1
        return result