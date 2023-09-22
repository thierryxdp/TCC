# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que substitui um elemento da string "s" na posição "i" pelo caracter "x"
    string,int,int->string"""
    return s[0:i-1]+str(x)+s[i+1:]