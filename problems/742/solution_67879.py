# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str, int -> string
def substitui(s,x,i):
    """retorna uma string s, igual a s onde o elemento na posição i é igual a x. (str,str,int->str)"""
    return str(s[0:i]+x+s[(i+1):])