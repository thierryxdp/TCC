def busca(setor, matriz):
    """Recebe uma matriz com dados e retorna os dados que são pedidos.
       list -> list"""
    pessoas = []
    
    for i in range(0, len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            list.append(pessoas, matriz[i])
    
    return pessoas