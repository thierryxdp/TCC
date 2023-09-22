# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "retorna uma string s com o elemento da posição i substituído pelo caractere x"
    return str(s)[0:(i):1]+str(x)+str(s)[(i)::]