# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "substitui caractere da entrada de s(string) por x(caractere modificante) na posição i da string"
    return s[0:i-1]+x+s[i+1:]