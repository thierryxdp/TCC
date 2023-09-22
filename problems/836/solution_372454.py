def busca(setor,matriz):
  
    funcionario = [] 
    total = []
    for i in range(len(matriz)):
        if i[2] == setor:
            del i[2]
            funcionario = funcionario + [matriz[i]]
            
            total = total + funcionario
            
    return total