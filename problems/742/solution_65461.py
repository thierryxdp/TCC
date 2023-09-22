# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que retorna uma string 
    s, com o elemento da posição i trocado
    pelo caractere x"""
    return s[0:i] + x + s[i+1:]