def uppCons(frase):
    """Recebe uma frase e retorna a frase com as consoantes
    	em maisculo
        str --> str"""
    vogais = 'AEIOUaeiou'
    i = 0
    while i < len(frase):
        if frase[i] not in vogais:
            frase = str.replace(frase, frase[i], str.upper(frase[i]))
        i = i + 1
    return frase