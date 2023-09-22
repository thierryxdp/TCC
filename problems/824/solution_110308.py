def uppCons (frase):
    '''função que recebe uma frase e retorne essa mesma frase
    com todas as consoantes em maiúsculas.
    string -> string'''
    letra = 0
    final = ''
    while letra < len(frase):
        if frase[letra] not in ('a','A','E','e','i','I','o','O','u','U'):
            final += frase[letra].upper()
        else:
            final += frase[letra]
        letra += 1

    return final