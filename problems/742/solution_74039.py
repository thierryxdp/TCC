# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(str1,x,i):
    """função recebe um string s, um caractere x e um número  inteiro i e retorna uma string igual a s, com o elemento da posição i substituído pelo caractere x."""
    return str1[0:i]+x+str1[i+1]