# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função definida por substitui(s, x, i) que receba uma string s,
    um caractere x e um número inteiro i entre 0 e o comprimento da string,
    e retorne uma string igual a s, exceto que o elemento da posição i deve ser
    substituído pelo caractere x"""
    e=len(s)
    v=e.replace('x','i')
    return v