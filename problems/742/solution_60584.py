# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Esta funcao retorna uma string igual a 's', onde a posicao i deve ser substituida pelo caractere x 
    recebe uma string 's', um numero inteiro 'i' que é entre 0 e o comprimento da string.""" 
    l=list(s)
    l[i]=x
    return "".join(l)