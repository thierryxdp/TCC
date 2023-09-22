def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    que contem as mesmas palavras da frase de entrada
    na ordem inversa sem maisculas e pontuação.
    string -> string'''
    low = frase.lower()
    separa = low.split()
    l_frase = []
    for palavra in separa:
        l_frase += [palavra]
    return l_frase