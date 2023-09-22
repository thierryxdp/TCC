# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe ums string, um caractere x e um número inteiro i e retorna uma
       string igual a s com elemento da posiçao i substituido pelo caractere x
       str,str,int->str
       Parâmetros:
       s: string
       x: caractere
       i: len(s)
    """
    return s[0:i]+x+s[(i+1):]