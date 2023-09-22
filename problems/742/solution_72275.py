# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'substitui o caractere na posição i da string s pelo caractere x'
    return s[0:(i-1)]+str(x)+s[i:]