# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i < len(s)-2:
        return s[0:i]+x+s[i+1:]
    else:
        return s[0:i]+x