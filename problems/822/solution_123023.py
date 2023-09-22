def repetidos(lista):
'''recebe uma lista como entrada e retorna o numero de vezes que o elemento
    da lista é igual ao elemento anterior'''
    i=0
    repetidos = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetidos.append(lista[i])
        i=i+1
    return len(repetidos)