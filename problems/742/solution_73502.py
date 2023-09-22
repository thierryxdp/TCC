# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que dado uma string s, um caractere x e 
    um número inteiro i entre 0 e o comprimento da string retorne uma string
    igual a s, excete que o elemento da posição i deve ser substituido pelo caractere x;
    str, int,int->str'''
    b=i+1
    return s[0:i]+x+s[b:]