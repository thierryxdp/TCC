def substitui (s,x,i):
    """ retorna uma string s, que teve seu elemento da posição 'i' substituído
    pelo caractere 'x'"""
    a = s.replace (s[i],x) if 0<=i<=len(s)
    return a