def repetidos(lista):
    'Dado uma lista de números, verifica quantas vezes um elemento é igual ao elemento anterior. Entrada: lista[int/float]. Saídas: int.'
    #O enunciado não indica se a lista é apenas com números inteiros.
    pos=1
    resutado=0
    while pos<len(lista):
        if lista[pos-1]==lista[pos]:
            resultado=resultado+1
        pos=pos+1
    return resultado