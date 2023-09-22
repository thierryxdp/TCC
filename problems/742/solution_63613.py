# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui o caractere na posição i pelo x informado
    str,str,int -> str
    s[i] == x
    return str(s[0:i]) + str(x) + str(s[i+1:])