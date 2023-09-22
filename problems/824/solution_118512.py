def uppCons (frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiúsculas.
       str -> str
    '''
    i=0
    while i<len(frase):
        if frase not in 'aeiou':
            str.lower(frase)
            frase = frase[i]
        i = i + 1
    return frase