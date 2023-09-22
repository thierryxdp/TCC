def uppCons(frase):
    """
    Retorna uma frase com as consoantes maiúsulas.
    str-> str
    """
    cmasc=''
    i=0
    excluidos=[',','.',';',':','?','-','!','a','e','i','o','u']
    while i<len(frase):
        if frase[i] in excluidos:
            cmasc= cmasc+frase[i]
        else:
            cmasc= cmasc+frase[i].upper()
	i=i+1
    return cmasc