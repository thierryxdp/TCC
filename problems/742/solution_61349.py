# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui o a letra de indice 'i' na string 
    pelo caractere x;
    str, str, int -> str"""
    return s[ : i ] + str(x) + s[ i + 1: ]