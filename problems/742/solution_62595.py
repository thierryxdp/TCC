# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    funcao que substitui caracteres em uma determinada string
    parametros:
    s--->str
    x--->str
    i--->int
    saida:
    str
    '''

    s=str(s)
    x=str(x)
    #0<=i<=len(s)

    if i==0:
        return x + s[1:]
    elif i==len(s):
        return s[0:i-1] + x
    elif 0<i<len(s):
        return s[0:i] + x + s[i+1:]