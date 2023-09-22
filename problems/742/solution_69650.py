# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
        str, int, int -> str
    '''
    0 <= i <= len(s)
    s[i] == x
    return s[0:i] + s[i] + s[i+1]