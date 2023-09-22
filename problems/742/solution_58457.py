# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que dada uma string s troque o caractere da posição i por um caractere definido por x'''
    sub_s1=s[0:i]
    sub_s2=s[i+1:]
    
    return sub_s1+x+sub_s2