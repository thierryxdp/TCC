# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'função que retorna o valor de s, sendo, str(i) substituido por str(x)'
    s[i]=x
    return s[0:i]+x+s+s[i+1:]