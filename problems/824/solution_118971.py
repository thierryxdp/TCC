def uppCons(frase):
    """Recebe uma frase e retorna a frase com as consoantes
    	em maisculo
        str --> str"""
    cons = 'bcdfghjklmnpqrstvxywzçBCDFGHJKLMNPQRSTVXYWZÇ'
    i = 0
    while i < len(frase):
        if frase[i] in cons:
            frase = str.replace(frase, frase[i], str.upper(frase[i]))
        i = i + 1
    return frase