def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    que contem as mesmas palavras da frase de entrada
    na ordem inversa sem maisculas e pontuação.
    string -> string'''
    l_frase = frase.split()
    inverte = l_frase[::-1]
    return inverte