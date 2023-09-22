def hashtag(s):
    ''' funcao que dada uma string (s) retorna uma insere um # no comeco,no meio e no fim da string'''
    return str('#') + s[0:len(s)//2] + str('#') + s[len(s)//2:] + str('#')