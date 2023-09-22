def busca(setor, m):
    """Retorna uma lista contendo os dados de todos os
    funcionários de um determinado setor dado como entrada, 
    a partir de uma matriz de funcionários de uma empresa
    também dada como entrada.
    str, list(list) -> list"""
    lista = []
    for l in range(0,len(m)):
        if str.lower(m[l][2]) == str.lower(setor):
            dados = list.copy(m[l])
            del dados[2]
            list.append(lista,dados)
            
    return lista