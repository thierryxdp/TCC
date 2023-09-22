# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''a função substitui a str na posição i pela string x. str,str -> i'''
    if s[i]== s[-1]:
        return s[0:i]+x+s[i+1:-1]
    else:
        return s[0:i]+x+s[i+1:-1]+s[-1]