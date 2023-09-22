# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui um elemnto da string s pelo caractere x na posição i; sting, string, int -> string'''
    sub1=s[0:i]
    sub2=s[i+1:-1]
    return str(sub1+x+sub2)