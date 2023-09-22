# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string (s) e substitui o elemento da posição(i) pelo caractere(x)'''
    '''3string,int,int->string'''
    s=list(s)
    s[i]=x
    return ''.join