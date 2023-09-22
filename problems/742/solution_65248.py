# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna dentro de um string o caractere 
    na posição indicada por i por outro carectere dado por x
    str,int,int->str'''
    termos_palavra= len(s)
    corte=s[0:i]
    sobra=s[i+1:termos_palavra]
    return corte+x+sobra