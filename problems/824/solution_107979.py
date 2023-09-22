def uppCons(frase):
    ''' Retorna uma frase com todas as suas consoantes em maiusculo'''
    
    frase1 = ""
    i = 0
    while i < len(frase):
        if frase[i] not in "aeiouAEIOU":
            frase1 = frase1 + frase[i].upper()
        return frase1