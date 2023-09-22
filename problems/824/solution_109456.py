def uppCons(frase):
    """ Função que recebe uma frase, e retorna todas as consoantes em maiusculo.
    str - > srt """
    c = 0
    nova_frase = ''
    while c < len(frase):
        if frase[c] not in 'aeiouãéíóú':
            nova_frase += frase[c].upper()
        else:
            nova_frase += frase[c].lower()
        c += 1

    return nova_frase