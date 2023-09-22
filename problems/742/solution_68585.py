# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Essa função tem como objetivo substituir um caracter de uma srt'''
    return s[:i]+x+s[(i+1):len(s)]