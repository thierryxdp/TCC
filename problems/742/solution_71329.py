# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x
    str,int->str"""
    l = [s,x,i]
    l[2] = x
    return str(s) or l