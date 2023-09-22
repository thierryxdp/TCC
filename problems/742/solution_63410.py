# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string (s), um caractere (x) e um número
    inteiro (i) e retorna uma string igual a s, exceto que o
    elemnto da posição i deve ser substituído po x'''
    str(s[i]) = x
    return str(s[0:i]) + str(x) + str(s[i+1:])