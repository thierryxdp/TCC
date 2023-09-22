# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função recebe uma string e substitui o eltho i pelo caracter X
    string,int,int->string
    """
    return s[:i] + x + s[i+1:]