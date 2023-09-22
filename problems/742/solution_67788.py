# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Troca o elemento na posição i pelo caracter x numa string s"""
    """string, int, int -> string"""
    tupla2 = s[:i] +str(x)+ s[1+i:]
    return tupla2