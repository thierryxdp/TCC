# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna a string possuindo a str no meio da mesma
       str->str"""
    s=str(s)
    return s[0:2]+s+s[2:]