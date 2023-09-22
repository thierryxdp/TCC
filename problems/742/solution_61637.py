# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''A partir da string s ira retorna-la com o caractere que estiver na 
    posicao i(lembre que o primeiro caractere e 0, o segundo 1,...)
    substituido pelo caractere x
     str,int,int -> str ou str,str,int ->str'''
    return s[0:i]+str(x)+s[(i+1):]