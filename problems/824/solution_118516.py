def uppCons (frase):
    '''
       Dada uma frase a função retorna a frase com as 
       consoantes em maiúsculas.
       str -> str
    '''
    i=0
    while i<len(frase):
        if frase not in 'aeiou':
            return str.upper(frase[1])
        i = i + 1
    return frase