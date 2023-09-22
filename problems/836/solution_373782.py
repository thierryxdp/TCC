def busca(setor:str, matriz:list)->list:
    """Recebe uma matriz e faz busca por setor, dando os dados dos funcionários"""
    y=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            y=y*[matriz[i]]
    return y