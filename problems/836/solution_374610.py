def busca(setor, matriz):
 def busca(setor, matriz):
    
    banco_dados =[]
    i=0
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = matriz[i]
            
            banco_dados = funcionario[:]
            
            banco_dados.append(banco_dados)
        if setor not in matriz[i]:
            banco_dados.append([])
            
    return banco_dados