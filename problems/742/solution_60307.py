# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
   '''dado S,X,I, ira retorna um str = s, com a posição i substituiído pelo x.'''
    return s[0:i]+x+s[i+1:]