# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i==0:
        return x+s[1:len(s)]
    else:
        return s[0:i]+x+s[i:len(s)]