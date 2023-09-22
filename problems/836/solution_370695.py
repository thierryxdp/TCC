def busca(setor, matriz):
    """Função que dado uma matriz com os dados dos funcionários de uma
    empresa e o setor(setor) da empresa, retorne os dados de todos os
    funcionários que trabalham nesse setor.
    string, lista -> lista"""
    
    solucao = []
    
    for info in range(len(matriz)):
        if str(setor) in str(matriz[info][2]):
            list.append(solucao, matriz[info])
            list.pop(2)
        
    return solucao