# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    0<int(i)<len(s)
    return (s[0:i]-s[i])+'x'+s[i:len(s)]