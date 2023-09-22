# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que recebe um caractere x e um numero inteiro i entre 0 e o tamanho da string e retorne uma string onde a posição i é substituída pelo caractere x"""
    return str(s[0:i]+str(x)+s[i+1:])