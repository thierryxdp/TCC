def substitui (s,x,i):
    """ retorna uma string s, que teve seu elemento da posição 'i' substituído
    pelo caractere 'x'"""
    return ''.join(x if c == s[i] else c for c in s)