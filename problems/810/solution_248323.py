def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    que contem as mesmas palavras da frase de entrada
    na ordem inversa sem maisculas e pontuação.
    string -> string'''
    low = frase.lower()
    separa = low.split()
    reverte = separa[::-1]
    tupla = tuple(reverte)
    nova_tupla = ' '.join(tupla)
    
    dnv = []
    kkkk = nova_tupla.split()
    for palavra in kkkk:
        dnv += [palavra]
    return palavra