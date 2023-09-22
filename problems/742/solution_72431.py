# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' função que recebe uma string, um caractere e um 
     numero , entre 0 e o comprimento da string, retornando
     uma string igual a s, exceto que o elemento da posição do 
     inteiro deve ser substituido pelo caractere x ;
      string, int,int -> string'''
         return s[:i] + x + s[i+1:]