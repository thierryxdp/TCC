# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui um caractere de uma string por um novo caractere, dado a string s, o novo caractere x e o indíce da posição da substituição i;str,int,int->str'''
    return s[0:i]+str(x)+s[(i+1):]