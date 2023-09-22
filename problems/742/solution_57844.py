# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui dentro da string s o caractere x dentro da posição i, o valor de i deve estar contido dentro do comprimeto da string s
    	str, int, int -> str'''
    if i<= len(s):
        return s[:i:] + "x"
    else:
        return()