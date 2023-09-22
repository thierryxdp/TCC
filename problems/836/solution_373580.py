def busca(setor ,matriz):
    resultado=[]
    i=0
    while i < len(matriz):
        if setor in matriz[i][2]:
            resultado =resultado + matriz[i]
        i +=1    
    return resultado