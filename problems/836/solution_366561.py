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
    	linha = del matriz[indice][2]
        resultado.append(linha)
    return resultado