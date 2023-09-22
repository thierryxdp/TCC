def busca(setor, matriz):
    '''Função que tendo como entrada o nome de um setor da empresa e uma
    matriz com os dados dos funcionários, retorna os dados de todos os 
    funcionários daquele setor
    str, list -> list'''
    result=[]
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            list.append(result,matriz[i])
    return result