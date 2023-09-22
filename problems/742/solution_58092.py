# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado como entrada uma string s, um caractere x e um inteiro i,
    retorna uma string igual a s, exceto que o elemento da posição i
    deve ser substituido pelo caractere x;
    string, int, int -> string"""
    return s[0:i] + x + s[i + 1:]