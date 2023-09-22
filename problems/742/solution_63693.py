# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui um caractere x no número inteiro i da string principal, i deve ter no maximo o comprimento da string;
    str,str/float,int->str'''
    return s[:i]+str(x)+s[i+1:]