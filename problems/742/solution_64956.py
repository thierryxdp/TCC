# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s, onde o elemento da posição i é
    substituído pelo caractere x"""
    
    return str(s)[0:i]+x[i:]