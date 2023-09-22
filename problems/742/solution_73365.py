# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    n = len(s)
    l = s.find(s[i:i+1])
    if l==i:
        return s.replace(s[l:l+1],x)
    else:
        return s