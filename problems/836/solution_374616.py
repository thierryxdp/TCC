def busca(setor, matriz):
    
    banco_dados =[]
    i=0
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = matriz[i]
            
            banco_dados = funcionario[:]
            
            banco_dados.append(banco_dados)
    del banco_dados[3]        
    return banco_dados