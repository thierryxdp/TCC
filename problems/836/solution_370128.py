def busca(funcao,lista):
    c=[]
    for i in range(len(lista)):
        if funcao==lista[i][2]:
            c=c+[lista[i][0:2]+lista[i][3]]
    return c