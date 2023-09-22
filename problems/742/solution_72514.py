# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string e altera um de seus caracteres por 
    outro (x), em uma posiçõa específica da string (i)'''
    ''' str, str, int->str'''
    return s[0:i] + x + s[(i+1):]