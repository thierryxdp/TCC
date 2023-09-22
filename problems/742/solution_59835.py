# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que retorna uma string s com o elemento da posicao i substituido pelo caractere x, sendo i um numero inteiro entre 0 e o comprimento da string"""
    return s[:i] + x + s[i+1:len(s)]