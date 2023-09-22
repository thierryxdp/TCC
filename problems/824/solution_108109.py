def uppCons(frase):
    """Essa funcao, dada uma frase, retorna a frase com todas as suas
	 consoantes em maiúsculo str -> str"""
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz' and 'BCDFGHJKLMNPQRSTVXWYZ':
            frase = frase.replace(frase[i],frase[i].upper())
        i = i + 1
    return frase