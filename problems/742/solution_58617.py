def substitui (s,x,i):
    """ retorna uma string s, que teve seu elemento da posição 'i' substituído
    pelo caractere 'x'"""
    a= s.replace(s[len(s)],x, len(s))
    return a