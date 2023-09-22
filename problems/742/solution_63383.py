# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'Retorna uma string igual a s, mas com o caractere x na posicao i, com 0<=i<=int(len(s)). Str, str, int -> str
    return [0:i]+x+s[(i+1):]