def posLetra(uma_string, letra, n):
    '''Função que recebe como entrada uma string, uma letra e um numero n inteiro que indica a ocorrencia desejada, e retorna em que posição da string a ocorrencia da letra está.'''
    '''str, str, int -> int'''
    encontrar = str.find(uma_string, letra)
    while n > 1:
        if encontrar >= 0:
            encontrar = str.find(uma_string, letra, encontrar + 1)
        n -= 1
    return encontrar