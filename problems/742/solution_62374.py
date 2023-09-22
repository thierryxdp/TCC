# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que recebe uma string s,um caractere x e um numero intero i entre 0 e ocomprimento da string,e retorne uma string igual a s,exceto que o elemento da posicao i deva ser substituido pelo caractere x;str,st->str"""
    return s[:i] + x +s[(i + 1):]