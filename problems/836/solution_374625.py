def busca(setor, matriz):
    
    banco_dados =[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = matriz[i]
            
            banco_dados = funcionario[:]
            del banco_dados[2]
            
            
        
    return banco_dados