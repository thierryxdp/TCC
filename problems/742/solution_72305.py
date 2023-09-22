# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna uma string igual a variavel s,
    exceto que o elemento da posição i deve ser 
    substituido pelo caractere x.
    str; int, int -> str.'''
    return s[i-1]+str(x)+s[i+1]