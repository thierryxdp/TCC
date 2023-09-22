def repetidos(lista):
    '''recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é
    igual ao elemento anterior'''
    inicio = 0
    seguinte = 1
    total = (len(lista) - 1)
    repeticoes = []
    
    while inicio < total:
        if lista[inicio] == lista[seguinte]:
            repeticoes = repeticoes + [inicio] # a = valor generico para representar a repetição
        inicio = inicio + 1
        seguinte = seguinte + 1

    return len(repeticoes)