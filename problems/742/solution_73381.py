# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    n = len(s)
    b = s.count(s[i:i])
    l = s.find(s[i:i+1])
    if l==i and b==1:
        return s.replace(s[i:i+1],x)
    elif l==i and b!=1:
        return s
    else:
        return s