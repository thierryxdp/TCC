def uppCons (frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiúsculas.
       str -> str
    '''
    i=0
    while i<len(frase):
        if consoante not in 'aeiou':
            return str.upper(consoante)
        i = i + 1
    return frase