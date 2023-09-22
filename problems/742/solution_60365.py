# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """troca um caractere na string s pelo caractere definido
    por x, de acordo com o índice definido por i."""
    snovo = s[:i]+x+s[i+1:]
    return snovo