# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui (s,x,i):
    '''Função que altera uma frase de informações (s = str, x= str e i = int) de entrada: str, str, int -> str'''
    return s[:i] + x + s[i+1:]