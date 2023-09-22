def uppCons(frase):
    """
    Essa função recebe uma frase e retorna ela com todas suas 
    consoantes maísculas, mantendo os demais caracteres como estavam;
    str -> str
    """
    vogais = 'aeiou'
    str1 = ''
    for x in frase:
        if not x in vogais:
            str1 += x.upper()
            continue
        str1 += x
    return str1