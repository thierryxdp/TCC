# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'str,str,int->str'
    #função que altera uma string em determinada posição
    return s[:i] + x + s[i+1:]