# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma string igual a s e substitui pelo caractere x'''
    t=s[0:i]
    t=t+str(x)
    return t+s[i+1:]