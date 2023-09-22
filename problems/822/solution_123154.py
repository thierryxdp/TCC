def repetidos(lista):
    '''Função que recebe uma lista de numeros como entrada e retorna quantas
vezes um numero da lista é igual ao anterior
list -> int'''
    i= 0
    quant= 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            quant= quant + 1
        i= i + 1
    return quant