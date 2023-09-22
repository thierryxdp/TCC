def busca(matriz,setor):
    """Recebe uma matriz de quatro entradas e onome de algum setor, o
       qual é um dos elementos da matriz, eretorna os dados de todos
       os funcionários daquele setor
       parâmetros de entrada:list(list),str
       parâmetrosde saída:list(list)"""
    funcionarios=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for aij in matriz:
        if (aij[2]==setor):
            list.append(funcionarios,aij[0:2]+aij[3])                    
    return funcionarios