# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string "s" dada, após trocar o elemento que está na posição "i" pelo caractere dado "x". Observação: a posição "i" fornecida deve ser um número entre 0 e o comprimento da string."""
    return s[:i-1]+x+s[i:]