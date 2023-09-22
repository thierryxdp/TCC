# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string (s) e retorn essa string substiuindo o caractere na posição (i) pelo caractere (x)'''
    return str([:i+1]) + str([i:])