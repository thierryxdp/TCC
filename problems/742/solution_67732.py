# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """a função recebe uma string s,um caractere x e um número entre 0 e o comprimento da string, retornando a string com o caractere na posição do número i"""
    #str,int,int ->str#
    i=[0,len(s)]
    var=s
    var[i]=x
    s=var
    
    return str(s)