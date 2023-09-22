def uppCons (frase):
    '''função que recebe uma frase e retorne essa mesma frase
    com todas as consoantes em maiúsculas.
    string -> string'''
    letra = 0
    final = ''
    while letra < len(frase):
        if frase[letra] not in ('a','A','ã','Ã','á','Á','â','Â','E','e','é','É','ê','Ê','i','I',
                                'í','Í','o','O','ô','Ô','õ','Õ','ó','Ó'
                                'u','U','ú','Ú'):
            final += frase[letra].upper()
        else:
            final += frase[letra]
        letra += 1

    return final