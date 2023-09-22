def hashtag(s):
    ''' funcao que recbe uma string e retorna a mesma com 3 #, no inicio, no final e no meio, respectivamente;
    str -> str '''
    meio = len(s)//2
    return 's' + s[0:meio] + 's' + s[meio:len(s)] + 's'