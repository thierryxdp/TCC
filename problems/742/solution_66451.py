# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, string, int -> string
def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna s, exceto que o elemento da posição i será substituido por x'''
    return str(s)[:i]+'x'+[i:]