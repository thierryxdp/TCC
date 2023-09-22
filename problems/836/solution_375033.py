def busca(setor, matriz):
    '''função que recebe uma matriz composta por dados de diferentes pessoas de uma empresa e um setor da empresa, retorna todos os funcionários daquele setor
       str, list -> list'''
    i=0
    resp=[]
    while i<len(matriz):
        if setor in matriz[i][2]:
            del matriz[i][2]
            list.append(resp, matriz[i])
        i=i+1
    return resp