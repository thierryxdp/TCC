# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui recebe uma string(s), um caractere(x) e um numero inteiro(i) e devolve a string recebida com a troca do caractere do elemento da posição i pelo novo caractere x.
    str,str,int-->str'''
    string1=s[ :i]
    f=i+1
    string2=s[f: ]
    return string1+x+string2