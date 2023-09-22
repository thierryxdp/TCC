def busca("contalidade",matriz):
    lista=[]
    
    for i in matriz:
        if i[2]=="contabilidade":
            i.remove("contabilidade")
            lista.append(i)
    return lista