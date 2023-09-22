# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna uma string com o elemento da prosição i substituido por um caractere x'''
    return s[:i-1] + str(x) + s[i+1:]