def hashtag(s):
    ''' função que recebe uma string e retorna a mesma com 3 #, no inicio, no final e no meio, respectivamente;
    str -> str '''
    meio = len(s)//2
    return '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'