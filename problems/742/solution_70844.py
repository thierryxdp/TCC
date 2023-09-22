# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' retornar uma string igual a s, menos quando a posição for i pois deve retorna x; string, int, int> string'''
    return s[0:i]+ x+ s[i+1:len(s)]