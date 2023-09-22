def substitui(s,x,i):
    ''' funcao que retorna a substituicao de um carater na string
    string, int, int -> string
'''
    s = s[0:i] + x + s[i + 1:]
    if s[0:i] + x + s[i + 1:]:
        return str(s)
    else:
        return s