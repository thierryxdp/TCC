def busca(string, matriz):
    '''Função que busca por setor a fim de retornar uma lista
    com os dados de todos os funcionários daquele setor.
    str, list(list)'''
    linha=len(matriz)
    col=len(matriz[0])
    if string == matriz[0][0]:
        return [matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3]]
    elif string==matrizmatriz[1][0]:
        return [matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3]]                          
    elif string==matriz[2][0]:
         return [matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3]]                
    else:
        return []