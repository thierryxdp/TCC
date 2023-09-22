def concatenacao(palavra1, palavra2):
    '''funcao que retorna a concatenacao das duas strings de entrada, primeiro na
    ordem direta e depois na ordem inversa; str, str -> str'''
    frase = palavra1 + palavra2
    return frase + frase[::-1]