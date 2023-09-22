def repetidos(lista):
    '''funcao que recebe uma lista de numeros e retorna o numero de vezes que teve teve o maior numero repetido dentro da lista
    list>list'''
    i=0
    repeticoes=0
    while i<len(lista):
        if lista[i] == lista [i-1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes