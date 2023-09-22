# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ it returns string with the given element in the place of index"""
    if -len(s)<=i<=len(s) and type(i)==type(1):
        return s[:(i)]+str(e)+s[(i+1):]