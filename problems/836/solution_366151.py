def busca(matriz,setor):
    '''função que busca as informações dos funcionaros por setor'''
    lista=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            lista.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    if len(lista)==´:
        return "Nenhum registro encontrado"
    else:
        return lista