# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''str, str, int -> str'''
    if i<=len(s):
        return str(s)[:i]+str(x)+str(s)[i+1:] or str(x)+str(s)[i:] or str(s)[:i]+str(x)
    else:
        return str(s)