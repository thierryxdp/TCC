# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """dado uma string, um caractere e um numero inteiro entre 0 e o comprimento da string, retorna a string com o elemento indicado na posicao i substituido pelo caractere x;
    str, str, int -> str"""
    s=list(s)
    s[i]=x
    s="".join(s)
    return s