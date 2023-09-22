def busca(funcao,lista):
    c=[]
    for i in range(len(lista)):
        if funcao==lista[i][2]:
            list.remove(lista[i],funcao)
            c=c+[lista[i]]
    return c