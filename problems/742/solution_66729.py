# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    F = s[0:i] + x
    if s[i] == and (i + 1) != len(s):
        return F + s[(1+i):-1] + s[-1]
    elif s[i] == s[-1]:
        return F
    elif s[i] != s[-1]:
        return F + s[(1+i):-1] + s[-1]