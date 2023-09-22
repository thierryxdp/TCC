# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Define uma funçãoque substitu ias variaveis s,x,i por uma string igual a s,
    exceto que o elemento da posicao i deve ser substituido por pelo caractere x"""
    return s[:i]+x+s[i+1:]