# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''comentario'''
    string= str(s)
    numero1= int(i)
    carac1= s[0:i]
    carac2= s[-1:i]
    funcao= carac1+str(x)+carac2
    return funcao