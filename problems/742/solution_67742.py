# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma str igual a s substituindo x pela
    posição i da str
    str,str,int -> str'''
    return str(s)[0:i]+str(x)+str(s)[i+1:]