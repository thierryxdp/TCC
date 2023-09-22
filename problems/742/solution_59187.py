# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'Funcao que recebe uma string s, um caractere x e um numero inteiro i
    'entre 0 e o comprimento da string, e retorna a mesma string, mas substituindo
    'o elemento da posicao i pelo caractere x'
    x = s[i]
    return s[0:i] + x + s[i:]