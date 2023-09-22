#Função que recebe uma string S, caractere x e um numéro i.
#uma string não deixa de ser uma string após a substituição exigida.
def substitui(s,x,i):
    return s[:i]+x+s[1+i:]