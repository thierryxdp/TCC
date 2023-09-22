def busca(setor, matriz):
    """ função que recebe uma matriz e o setor ou nome que se deseja buscar e retorna todos os dados dos funcionarios daquele setor
    	entrada: str, lista
        saida: lista
    """
    
    lista_final = []
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if setor == linha[2]:
                lista_final.append(linha[0])
                lista_final.append(linha[1])
                lista_final.append(linha[3])
    return lista_final