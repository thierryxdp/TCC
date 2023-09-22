# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que dado os parametros, substitui o numero inteiro (i) pelo caractere (x)'''
        variavel = s[:i]+x+s[i+1:]
    return variavel