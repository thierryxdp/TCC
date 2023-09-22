def busca(setor, matriz):
    """Dada uma matriz com as informações dos funcionários e um determinado setor
       retorna todos os funcionários desta área.
       str, list -> list"""
    
    listaResultado = []
    
    for indice1 in range(len(matriz)):
        pivo = matriz[indice1]
        
        for indice2 in range(len(pivo)):
            if pivo[indice2] == setor:
                pivo.remove(setor)
                listaResultado += pivo
                
    return listaResultado