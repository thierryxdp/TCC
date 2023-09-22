# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Dada uma string s, um caractere x e um número inteiro i entre 0 e comprimento sa string, a função retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo caracterex"
    "string, int, int -> string"
    return s[0:i]+str(x)+s[i+1:]