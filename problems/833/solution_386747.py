def conta_numero(numero,matriz):
    lista=0
    for i in matriz:
        for j in matriz[i]:
            if numero in i[j]:
                lista+=1
    return lista