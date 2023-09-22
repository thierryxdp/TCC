def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    com as mesmas palavras da frase na ordem inversa
    sem letras maisculas, e sem pontuação
    string -> string'''
    nova = frase.lower()
    nova = frase[::-1]
    if '.' in nova:
        nova.replace('.','')
        return nova