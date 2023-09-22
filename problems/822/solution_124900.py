def repetidos(lista):
    '''Funcao recebe uma lista e retorna quantas vezes um numero nela é igual ao anterir
list -> int'''
    contador = 0
    repeticao = 0
    while (contador < len(lista)):
        if (lista[contador] == lista[contador - 1]):
            repeticao += 1
        contador += 1
    return repeticao