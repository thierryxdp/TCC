def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    que contem as mesmas palavras da frase de entrada
    na ordem inversa sem maisculas e pontuação.
    string -> string'''
    low = frase.lower()
    separa = low.split()
    reverte = separa[::-1]
    nova_tupla = tuple(reverte)
    
    return ' '.join(nova_tupla)