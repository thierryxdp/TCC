def busca(setor, matriz):
    
    resultado = []
    
    for pessoa in matriz:
        if setor in pessoa[2]:
            indice = matriz.index(pessoa)
            del matriz[indice][2]
            resultado.append(pessoa)
        else:
            pass
       
   	
    return resultado