def busca(setor,matriz):
  
    funcionario = [] 
    total = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            funcionario = funcionario + [matriz[i]]
            
            total = total + funcionario
            
    return total