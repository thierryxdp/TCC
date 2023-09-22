# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que dada a string, uma letra e um indice, substitui o elemento 
     correspondente ao indice pela letra x"""
    return s[0:i]+x+s[i+1:]