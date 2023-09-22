# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, exceto que o elemento da posicao i deve ser substituido pelo caractere x"""
    return replace(s,x,i-1)