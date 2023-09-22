def busca(setor, matriz):
    
    resultado = []
    
    for pessoa in matriz:
        if setor in pessoa[1]:
            resultado.append(pessoa)
        else:
            pass
       
   	
    return resultado