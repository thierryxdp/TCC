# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que dado uma string, um caractere e um inteiro, retorna uma string igual a s, exceto que o elemento da posicao i deve ser substituido pelo caractere. str,int,int->str'''
    len(s)
    a=s[0:i]
    b=s[i+1:]
    c= str(a+x+b)
    return c