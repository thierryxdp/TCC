def busca(setor, matriz):
    
    resultado = []
    
    for pessoa in matriz:
        if setor in pessoa[2]:
            del matriz[pessoa][2]
            resultado.append(pessoa)
        else:
            pass
       
   	
    return resultado