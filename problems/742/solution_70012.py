# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string igual a s, exceto que o 
    elemento da posição i deve ser substituído pelo 
    caractere x. são as entradas: s, x que é um caractere e 
    um número inteiro i.'''
    return s[0:i]+x+s[i+1:]