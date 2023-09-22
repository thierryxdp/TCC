def busca(setor, matriz):
    """ função que recebe uma matriz e o setor ou nome que se deseja buscar e retorna todos os dados dos funcionarios daquele setor
    	entrada: str, lista
        saida: lista
    """
    
    lista_final = []
    
    for linha in matriz:
        if setor == linha[2]:
            linha.remove(setor)
            lista_final.append(linha)
    return lista_final