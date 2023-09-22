def uppCons(frase):
    ''' Retorna uma frase com todas as suas consoantes em maiusculo'''
    
    frase1 = ""
    i = 1
    while i < len(frase):
        if frase[i] not in "aeiouAEIOUãÃõÕêÊôÔóÓáÁíÍéÉúÚ":
            frase1 = frase1 + frase[i].upper()
        else:
            frase1 = frase1 + frase[i].lower()
    	i = i + 1
    return frase[0].upper() + frase1