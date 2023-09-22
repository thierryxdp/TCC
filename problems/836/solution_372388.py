def busca(setor,matriz):
  
    
    funcionario = [] 
    total = []
    for i in range(len(matriz)):
        if M[i][2] == setor:
            funcionario.append(M[i])
        total.append(funcionario)    
    return total