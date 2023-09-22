def busca(setor, matriz):
    
    banco_dados =[]
    i=0
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = matriz[i]
            
            banco_dados = funcionario[:]
            del banco_dados[4]
            banco_dados.append(banco_dados)
            
    return banco_dados