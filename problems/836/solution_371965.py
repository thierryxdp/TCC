def busca(setor, matriz):
    '''Função que retorna uma lista com as informações de um setor da empresa registrado na matriz 
    string, list -> list'''
    infoSetor = []
    for linia in range(len(matriz)):
        
        if matriz[linia][2] == setor:
            del matriz[linia][2]
            list.append(infoSetor, matriz[linia])
            
    return infoSetor