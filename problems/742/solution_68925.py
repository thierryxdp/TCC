# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função recebe como entradas uma string, um caractere
    (na forma int) e um outro inteiro [entre 0 e o comprimento
    da string], e retorna uma string igual à string dada como
    entrada, porém com o elemento da posição informada sendo
    substituído pelo caractere dado."""
    t = s.replace(s[i], str(x), 0)
    return t