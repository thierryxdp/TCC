# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Calcula e retorna a substituição de um caracter x na posição i de uma string s.
    string, int, int -> string"""
    substituta = str (s)
    substituta [i] = x
    return substituta