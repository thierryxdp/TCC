def busca(nome,matriz):
    '''
    função que dado um nome de um setor de uma empresa e uma matriz,
    a função retorna a lista com os dados dos funcionários que pertencem aquele
    setor, a lista não inclui o nome do setor 
    list(list)-->list(list)
    '''
    resposta=[]
    for linha in matriz:
        for el in linha:
            if nome in linha and el==nome:
                list.remove(matriz[list.index(matriz,linha)],nome)
                resposta+= matriz[list.index(matriz,linha)]
    return resposta