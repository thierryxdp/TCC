def busca(setor,matriz):
  
    funcionario = [] 
    
    for i in range(len(matriz)):
        if i[2] == setor:
            del i[2]
            funcionario.append(i)
            
            
            
    return funcionario