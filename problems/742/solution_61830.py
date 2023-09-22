# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Substitui e retorna uma string igual a S, porém substituindo o elemento da posição i pelo caractere x. str,str,int->str"
    return s[0:i]+x+s[i+1:]