def busca(setor, matriz):
    
    resultado = []
    
    for pessoa in range(len(matriz)):
        if setor in pessoa[1]:
            resultado.append(pessoa)
        else:
            pass
       
   	
    return resultado