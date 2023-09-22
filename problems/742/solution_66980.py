# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string igual a 's' de entrada, mas com
       o caractere da posição 'i' substituído pelo caractere
       'x', ambos também de entrada;
       str, int, int -> str'''
    return s[:i]+'x'+s[i+1:]