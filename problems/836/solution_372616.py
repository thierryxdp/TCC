def busca(setor,matriz):
  
    funcionario = [] 
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            funcionario.append(matriz[i])
            
            
            
    return funcionario