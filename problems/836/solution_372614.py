def busca(setor,matriz):
  
    funcionario = [] 
    
    for i in range(len(matriz)):
        if matriz[2] == setor:
            del matriz[2]
            funcionario.append(matriz[i])
            
            
            
    return funcionario