def busca(setor, matriz):
    """ função que recebe uma matriz e o setor ou nome que se deseja buscar e retorna todos os dados dos funcionarios daquele setor
    	entrada: str, lista
        saida: lista
    """
    
    lista_final = []
    
    
    for linha in matriz:
        lista_auxiliar = []
        if setor == linha[2]:
            lista_auxiliar.append(linha[0])
            lista_auxiliar.append(linha[1])
            lista_auxiliar.append(linha[3])
            lista_final.append(lista_auxiliar)
    return lista_final