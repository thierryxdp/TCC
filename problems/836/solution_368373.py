def busca(setor,matriz):
    """Retorna os dados de todos os funcionários de um setor buscado
    	str, list -> list
        Parameters:
        setor: Setor desejado
        matriz: Matriz com as informações dos funcionários
        
        Returns:
        Os dados de todos os funcionários do setor buscado
    """
    resultado = []
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if setor == matriz [i][j]:
                dados = matriz[i]
                dados = dados.pop(index(matriz[j]))
                resultado.append(dados)
                
    return resultado