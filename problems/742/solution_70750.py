# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''string, int, int -> string'''
    '''a funcao toma uma string s e substitui o
    elemento na posicao i por x'''
    x = s[0:i] + x + s[i+1:]
    return x