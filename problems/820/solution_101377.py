def repetidos(lista):
    '''função que retorna a quantidade de vezes um elemento é igual ao elemento anterior dado uma lista de números.'''
    
    i = 1 
    repeticoes = 0 
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1 
    return repeticoes