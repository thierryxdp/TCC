def busca(setor, matriz):
    funcionario = []
    banco_dados =[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario.append(matriz[i])
            
            banco_dados = funcionario[:]
            
            
            
    del banco_dados[2]   
    return banco_dados