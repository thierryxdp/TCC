# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    b = s.count(s[i:i+1])
    l = s.find(s[i:i+1])
    n = list(s)
    if l==i and b==1:
        return s.replace(s[i:i+1],x)
    elif l==i and b!=1:
        n[i] = x
        strn = ''.join(n)
        return strn
    else:
        return s