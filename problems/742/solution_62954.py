# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s2 = str.split(s)
    if(len(s2)>i):
        s2[i] = x
    return particionado