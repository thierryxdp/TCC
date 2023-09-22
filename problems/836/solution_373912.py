def busca(setor,matriz):
    '''funcao que recebe um setor da empresa e uma matriz,
       retornando os dados de quem trabalha naquele determinado
       setor da empresa.
       str, list(list) -> list(list)'''
    banco= []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            x= matriz[i][0:2] + matriz[i][3:]
            list.append(banco,x)
    return banco