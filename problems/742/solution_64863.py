# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna a string substituida pelo caracter x na posicao i;
    	string,int,int -> string"""
    return str(s)[0:i] + x + str(s)[i+1:]