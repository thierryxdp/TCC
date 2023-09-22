def busca (setor, matriz):
    """Função que, dado o nome do setor de uma empresa, retorna os 
    dados de todos os funcionários daquele setor presentes na matriz 
    que também foi fornecida como segundo elemento da entrada."""
    """str, list-->list"""
    resultado=[]
    copia_matriz=list.copy(matriz)
    for i in copia_matriz:
        if setor in i:
            i.remove(setor)
            resultado+=[i]
    return resultado