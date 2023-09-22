# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna s exceto se x substituir i'''
    s = str(s)
    return s[:1] + x + s[i+1:]