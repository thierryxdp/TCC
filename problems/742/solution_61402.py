# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''a função substitui a str na posição i pela string x. str,str -> i'''
    a=s[0:i]+x+s[i+1:-1]+s[-1]
    if len(s)<len(a):
        return s[0:i]+x+s[i+1:-1]
    else:
        return s[0:i]+x+s[i+1:-1]+s[-1]