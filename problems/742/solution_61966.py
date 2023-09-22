# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a = len(s)
    return str(s[0:i])+str(x)+str(s[i+1:a])