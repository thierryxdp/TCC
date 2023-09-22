# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """Função que retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
    str, int, int -> string."""
    return s[0:i] + s + x[(i+1):]