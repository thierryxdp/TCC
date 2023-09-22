# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' função que retorna uma string igual a s substituindo a letra na posição i pelo caractere x(s=string,x=caracter,i=número inteiro entre 0 e o comprimento da string)
       string,int,int -> string'''
    s[i]=x
    return s