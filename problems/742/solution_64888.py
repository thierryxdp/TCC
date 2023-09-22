# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, um caractere x, que deve ser dado como string também, e um numero inteiro i (i tem que estar entre 0~o numero de caracteres totais de s) e
    devolve uma nova string com o caracter x na posição i da sting s; str, str, int -> str"""
    return s[0:i]+x+s[i+1:]