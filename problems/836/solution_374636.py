def busca(setor, matriz):
    
    banco_dados =[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            del banco_dados[2]
            
            banco_dados.append(matriz[i])
    
    
    for j in range(len(banco_dados)):
        if banco_dados[j][2] == setor:
            del banco_dados[j][2]
            
    return banco_dados