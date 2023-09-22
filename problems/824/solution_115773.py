def uppCons(frase):
    """ Função que dada uma frase, retorna as consoantes em letra maiúscula, sem alterar os demais caracteres
    str -> str """
    d='bcdfghjklmnpqrstvwxyz'
    i=0
    while i<len(frase):
        if frase[i] in d:
            frase=frase[0:(i)]+str.upper(frase[i])+frase[(i+1):]
        i=i+1
    return frase