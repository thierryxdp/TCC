# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma sring 's',um caractere 'x'e um numero 'i', e substitui o elemento da posicao 'i' pelo caractere 'x';str,str,int-->str'''
    return s[0:i] + str(x) + s[i+1:]