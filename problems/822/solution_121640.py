def repetidos(lista):
    '''função que verifica e retorna quantas vezes um elemento é igual ao seu antecessor, a partir de uma lista com esses números; list -> int'''
    
    i = 1
    igual = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            igual = igual+1
        i = i+1
    return igual