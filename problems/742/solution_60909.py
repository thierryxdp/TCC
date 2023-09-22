# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string(s), um caractere(x) e um numero(i) entre 0
    e o comprimento da string, retornando a string "s",
    sendo trocado o elemento da posição "i" pelo caractere "x";
    str, str, int -> str"""
    return s[:i]+x+s[i+1:]