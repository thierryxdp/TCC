# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string (s), porém, ao retorna-la, troca seu caractér na posição (i) pelo designado
pelo parametro (x); String; string -> string"""
    return s[0:i]+x+s[i+1:]