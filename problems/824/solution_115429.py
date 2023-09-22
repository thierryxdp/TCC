def uppCons(frase):
    """
    Retorna uma frase com as consoantes maiúsulas.
    str-> str
    """
    cmasc=''
    i=0
    while i<len(frase):
        if frase[i] in ',.;:?-!aeiou':
            cmasc=cmasc+frase[i]
        else:
            cmasc=cmasc+frase[i].upper()
	i=i+1
    return cmasc