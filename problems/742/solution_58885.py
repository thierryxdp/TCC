# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Susbstitui  caractere na palavra(s), na posição(i) pelo caractere(x)
    str,str,int ->str'''
    a = s[0:i]
    b = s[i+1:]
    return a + x + b