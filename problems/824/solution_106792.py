def uppCons(frase):
    """Retorna a frase com suas consoantes maiusculas. str-->str"""
    i=0
    nova_frase=""
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase = frase+str.upper(frase[i])
    return frase