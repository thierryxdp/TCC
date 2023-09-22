# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ recebe uma string s, un csractere x e um numero inteiro i entre 0 e o comprimento da string, e retirna uma string igual s com o elemento na posição i substituido por x """
    return s[0:i] + x + s[i + 1:];