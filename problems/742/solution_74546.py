# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função retorna uma string substituindo um caracter ao receber, 
    string, caracter e número indice do caracter a ser substituido."""
    y=list(s)
    y[i]=(x)
    z="".join(y)
    return(z)