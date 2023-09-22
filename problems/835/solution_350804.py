def melhor_volta(matriz):
    resultado = ()
    lista = []
    for i in matriz:
        lista2 = []
        for j in i:
            list.append(lista2,j)
            list.append(lista,min(lista2))
    melhor_resultado =min(lista)          
    quem_foi = list.index(lista,melhor_resultado)
    qual_volta = list.index(lista2,melhor_resultado)
    resultado += (quem_foi,melhor_resultado,qual_volta)
    return resultado