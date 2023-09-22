# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    A função retorna uma string s, onde, a caractere da posição i,
    é trocada pela caractere x
    (entrada = str, str, int / saída = str)
    '''
    return s[ : i] + x + s[i + 1 : ]