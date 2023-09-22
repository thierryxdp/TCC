# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebendo uma string, um caractere e um numero, retorna uma string, exceto o elemento que foi cortado que será substituido pelo caractere
    str,int->str'''
    
    return  s[:i] + str(x) + s[1+i:]