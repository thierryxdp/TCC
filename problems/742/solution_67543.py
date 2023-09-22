# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, e um caractere x de forma que o caractere de posição i
da string s é substituido pelo caractere x; str, str, int ou float."""
    nome = s[:i]
    posnome = s[i+1:]
    return str(nome) + str(x) + str(posnome)