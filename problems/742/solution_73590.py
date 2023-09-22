# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'função que retorna o valor de s, sendo, str(i) substituido por str(x)'
    s[i]=x
    return [0:i]+x+[i+1:]