def hashtag (s):
    ''' Função que recebe uma strig e retorna a mesma com o caractere '#'
    no início,no meio e no final dela
    str -> str '''

    metade = round (len(s)/2)
    menos_metade = metade - 1
    

    if metade %2 == 0:
     return '#' + s[:metade] + '#'+ s[metade:]+ '#'
    else:
        return '#' + s[:menos_metade] + '#' + s[menos_metade:]+'#'