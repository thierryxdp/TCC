def melhor_volta(matriz):
    resultado = ()
    for i in matriz:
        voltas = []
        lista = []
        for j in i:
            lista2 = []
            list.append(lista2,j)
            list.append(lista,min(lista2))
            list.index(voltas,min(lista2))
    melhor_resultado =min(lista)          
    quem_foi = list.index(lista,melhor_resultado)
    qual_volta = voltas[quem_foi]
    resultado += (quem_foi,melhor_resultado,qual_volta)
    return resultado