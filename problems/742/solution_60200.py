# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s, um caracter x e um numero
    inteiro ientre 0 e o comprimento da string s. devolve
    uma string igua a s, excetuado caracter do indice i, que deve 
    ser substituido por x'''
    l=list(s)
    l[i]=x
    return"".join(l)