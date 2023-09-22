# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s, exceto que o elemento da posicao 
       i sera substituido pelo caractere x informado
    """
    return s[0:i] + x + s[i+1:]