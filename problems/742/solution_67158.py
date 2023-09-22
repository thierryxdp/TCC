# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string com um caracter trocado
    str, int, int -> string"""
    sub1=s[0:i]+str(x)+s[:]
    return sub1