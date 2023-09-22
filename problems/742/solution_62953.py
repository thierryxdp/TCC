# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    particionado = str.partition(s)
    if(len(s)>i):
        particionado[i] = x
    return particionado