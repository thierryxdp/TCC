#retorna o n de vezes que um elemento da lista é igual ao elemento anterior
#list-->list
def repetidos(ls):
    x=0
    ft=ls[1:len(ls)]
    for i in range(len(ft)):
        if ls [i]==ft[i]:
            x=x+1
    return x