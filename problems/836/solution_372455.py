def busca(setor,matriz):
  
    funcionario = [] 
    total = []
    for i in range(len(matriz)):
        if matriz[2] == setor:
            del matriz[2]
            funcionario = funcionario + [matriz[i]]
            
            total = total + funcionario
            
    return total