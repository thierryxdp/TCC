def repetidos(listanumeros):
    '''Função que recebe uma lista de números e retorna quantas 
vezes dois números seguidos são iguais.
Entrada:
    listanumeros: list
Saída:
    int'''
    vezes = 0
    i = 1
    while i < len(listanumeros):
        if listanumeros[i] == listanumeros[i-1]:
            vezes += 1
        i += 1
    return vezes