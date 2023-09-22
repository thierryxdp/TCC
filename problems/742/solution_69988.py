# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função recebe uma string, um caractere e um número e retorna a sting com o elemento da posição do numero dado substituído pelo caractere; str,int,int->str'''
    m=list(s)
    m[i]=x
    s = ''.join(m)
    return str(s)