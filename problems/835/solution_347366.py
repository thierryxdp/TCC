def melhor_volta (matriz):
    """Recebe uma matriz com informações dos tempos das 
    voltas de 6 corredores, cada um com 10 voltas, e retorna
    de quem foi o menor tempo da volta, o tempo dessa volta
    e qual volta ela foi.
    list -> tuple"""
    corredor = 0
    volta = 0
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):         
            list.append (lista, matriz[i][j])        
        if min(lista) in matriz[i] and matriz[i] in matriz:
            volta = 1 + list.index(matriz[i], min(lista))
            corredor = 1 + list.index(matriz, matriz[i])
    return (corredor, min(lista), volta)