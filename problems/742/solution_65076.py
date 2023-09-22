# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que retorna a string s com o caractere x na posição i
    str,str,int -> str """
    return s[0:i]+x+s[i:]