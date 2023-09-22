# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string s recebida anteriormente com uma
    mudança na posiçãi i pela x'''
    j=i+1
    return s[0:i]+x+s[j:]