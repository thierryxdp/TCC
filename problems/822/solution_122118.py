def repetidos(lista):
    '''funcao que recebe como entrada uma lista de numeros, e retorna o numero de vezes 
    que um elemento da lista é igual ao elemento anterior.
    lista ->int'''
    i = 1
    repeticao = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repeticao = repeticao + 1 
        i = i + 1
    return repeticao