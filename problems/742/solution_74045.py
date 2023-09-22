# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função recebe um string s, um caractere x e um número  inteiro i e retorna uma string igual a s, com o elemento da posição i substituído pelo caractere x."""
    s[i] == x
    return s[0:i] + x + s[i + 1:]