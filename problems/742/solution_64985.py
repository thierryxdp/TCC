# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s, onde o elemento da posição i é
    substituído pelo caractere x"""
    
    parte1 = s[0:i]
    
    parte2 = s[i:]
    
    return parte1 + x + parte2