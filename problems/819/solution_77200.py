def multiplos(listanumeros, n):
    '''Função que recebe uma lista de números e um número inteiro
n e retorna quais números da lista são múltiplos de n.
Entradas:
    listanumeros: list
    n: int
Saída:
    list'''
    i = 0
    encontrados = []
    while i < len(listanumeros):
        if listanumeros[i]%n == 0:
            encontrados.append(listanumeros[i])
        i += 1
    return encontrados