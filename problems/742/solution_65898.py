# Retorna uma string, com a substituição de um caractere da string original por x.
# string, int, int -> string
def substitui(s,x,i):
    return s[0,i]+'x'+s[i+1,]