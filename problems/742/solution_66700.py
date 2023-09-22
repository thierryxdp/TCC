# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, str, int -> string
def substitui(s,x,i):
    B = s[0:1]+x
    if s[i]==s[-1] and (i+1) != len(s):
        return B+s[(i+1):-1]+s[-1]
    elif s[i]==s[-1]:
        return B
    elif not s[i]==s[-1]:
        return B+s[(i+1):-1]+s[-1]