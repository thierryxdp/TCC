# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Calcula e retorna a substituição de um caracter x na posição i de uma string s.
    string, int, int -> string"""
    substituta = str (s)
    pre = str (s) [0:len((str (s))//i)]
    pos = str (s) [len((str (s))//i):]
    substituta = pre + str(x) + pos
    return substituta