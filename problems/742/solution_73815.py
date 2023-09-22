# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' 
    Recebe uma string, um caracter e um inteiro
    Faz a substituição do elemento indicado fazendo uma separação pelo indice indicado
    '''
    s = s[:i] + x + s[i+1:]
    return s