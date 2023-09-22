# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao que recebe uma string(s), um caractere(x) e um numero inteiro(i), substitui o elemento da posicao i pelo caractere x e retorna uma nova string s.
    str,int,int-> str'''
    s=str(s)
    x=str(x)
    i=int(i)
    s1=s[:i]+x+s[i:]
    
    return s1