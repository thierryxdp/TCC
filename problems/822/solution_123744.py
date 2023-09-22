def repetidos(lista):
    '''função que retorna a quantidade de elementos iguais ao 
    seu anterior. list->int'''
    repeticao = 0
    i = 0
    j = 1
    while j < len(lista):
        if lista[j] == lista[i]:
            repeticao = repeticao + 1
        i = i + 1
        j = j + 1
    return repeticao