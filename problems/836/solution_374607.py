def busca(setor, matriz):
    
    banco_dados =[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = matriz[i]
            
            banco_dados = funcionario[i]
            del banco_dados[2]
            
            banco_dados.append[banco_dados]
    
    return banco_dados