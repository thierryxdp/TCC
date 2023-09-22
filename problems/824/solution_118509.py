def uppCons (frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiúsculas.
       str -> str
    '''
    frase = ''
    i=0
    while i<len(frase):
        if frase not in 'aeiou':
            str.lower(frase)
        i = i + 1
    return frase