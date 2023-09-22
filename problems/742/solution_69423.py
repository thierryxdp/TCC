# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Essa função recebe uma string, uma letra x e um numero i
    sendo que este representa o local no qual x vai trocar de lugar em s'''
    return s[:i] + x + s[i+1:]