def busca(setor,matriz):
  
    
    funcionario = [] 
    total = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            funcionario.append(matriz[i])
            total= total + funcionario  
    return total