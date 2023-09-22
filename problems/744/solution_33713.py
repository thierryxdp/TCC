def hashtag (s):
    ''' Função que recebe uma strig e retorna a mesma com o caractere '#'
    no início,no meio e no final dela
    str -> str '''

    import math
    metade = round (len(s)/2)
    mais_da_metade = (math.ceil(len(s)/2)-1)
    

    if len(s)%2==0:
        return "#" + s[:metade] + "#" + s[metade:] + "#"
    else:
        return "#" + s[:metade] + "#" + s[mais_da_metade:] + "#"