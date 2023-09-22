def busca(setor, matriz):
    '''
    Busca cadastros de funcionários de acordo 
    com o setor;
    string, list -> list
    '''
        
    setores = [linha[2] for linha in matriz]
    indices = [indice for indice, valor in enumerate(setores) if valor == setor]
    resultado = []
    for indice in indices:
    	resultado.append(matriz[indice][:2].extend(matriz[indice][3]))
    return resultado