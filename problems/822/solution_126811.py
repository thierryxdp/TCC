def repetidos(lista):
    """funcao que recebe uma lista e conta quantos
    numeros dela sao repetidos; list-> int"""
    contagem=1
    resultado=0
    while contagem<len(lista):
        if lista[contagem]==lista[contagem-1]:
            resultado+=1
        contagem+=1
    return resultado