def busca():
    resultado = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                matriz[i].remove(setor)
                resultado.append(matriz[i])
                
    return resultado