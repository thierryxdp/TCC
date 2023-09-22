# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' substitui um elemento na posição i de s por x
string, int, int -> string'''
    s= s[0:i]+str(x)+s[i+1:]
    return s