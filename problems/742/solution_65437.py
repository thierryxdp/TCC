# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que substitua i por x e retorne uma string igual a s'''
    return s[0:i]+x+s[i+1:]