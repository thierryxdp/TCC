def busca(setor,matriz):
    ''''''
    indice=0
    
    
    while indice<len(matriz):
        if setor in matriz[indice][0]:
            resultado=resultado+[lista[indice]]
        indice=indice+1
    return resultado