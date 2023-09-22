import re
def substitui (s,x,i):
    """ retorna uma string s, que teve seu elemento da posição 'i' substituído
    pelo caractere 'x'"""
    a = re.sub (s[i],s,x)
    return a