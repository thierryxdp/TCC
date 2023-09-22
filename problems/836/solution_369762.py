def busca(setor,matriz):
    """
    Função que recbe um setor e uma matriz e retorna os dados das pessoas
    dese setor.
    str, lis -> list
    
    Parâmentros:
    Entrada: setor
    		 matriz
    
    Retorna: lista de pessoas
    """
    
    lista=[]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                linha=[]
                pessoa = matriz[i][j-2]
                linha.append(pessoa)
                registro = matriz[i][j-1]
                linha.append(registro)
                telefone = matriz[i][j+1]
                linha.append(telefone)
        		lista.append(linha)
                
    return lista