# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que dado uma string 's',um caractere
    'x' e um numero 'i', retorna uma string em que
    o caractere foi incerido na posicao i;
    str,str,int -> str'''
    return str(s)[0:i-1] + str(x) + str(s)[i:]