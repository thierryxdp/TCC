# 
# Escolha nomes elucidativos para suas variáveis
# str, str, int -> string
def substitui(s,x,i):
    if i=0:
        return x+s[1:]
    else s[0:i]+x+s[i:]