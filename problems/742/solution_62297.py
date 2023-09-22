# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna a string subtituída com os padrões requeridos
       str,int,int->str"""
    s=str(s)
    return s[0:i]+str(x)+s[i+1:]