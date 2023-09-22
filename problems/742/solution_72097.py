# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função recebe uma string s, e substitui nela o caractere de
    posição i pelo caractere x"""
    '''
    s = () "string
    x = i
    i = len (s)
    string, int, int --> string'''
    var0=str(s)
    var1=var0[0:i]
    var2=var0[i+1:]
    return str(var1)+str(x)+str(var2)