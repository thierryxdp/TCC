def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    que contem as mesmas palavras da frase de entrada
    na ordem inversa sem maisculas e pontuação.
    string -> string'''
    low = frase.lower()
    separa = low.split()
    invertida = separa[::-1]
    listas = []
    for palavras in invertida:
        listas += [palavras]
    return listas