def uppCons(frase):
    '''Dada uma frase retorna a mesma com suas consoantes maiúsculas 
    str -> str'''
    c = 0
    while c < len(frase):
        if frase[c] not in 'aeiou':
            str.upper(frase[c])
   		c += 1
    return frase