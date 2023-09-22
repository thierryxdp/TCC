# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo caractere x. onde s é a string, x o caractere, e i um número inteiro entre 0 e o comprimento da string; string, int, int -> string''' 
    return(s[:i]+x+s[i+1:])