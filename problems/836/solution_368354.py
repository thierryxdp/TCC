def busca(setor:str,m:list)->list:
    """função que recebe uma matriz com os dados de funcionários da empresa e, dado o nome de um setor da empresa,
    retorna os dados dos funcionários desse setor
    
    parametros:
    str, list -> list"""
    acumulador=[]
    for i in range(len(m)):
        if m[i][2]==setor:
            acumulador.append(m[i])
            del acumulador[-1][-2]
    return acumulador