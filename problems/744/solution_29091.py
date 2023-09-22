def hashtag(s):
    '''Recebe uma string e insere o caractere "#" no
    início, no meio e no final dela
    str -> str'''
    calc_metade = len(s) // 2
    metade1 = s[:calc_metade]
    metade2 = s[calc_metade:]
    return '#' + metade1 + '#' + metade2 + '#'