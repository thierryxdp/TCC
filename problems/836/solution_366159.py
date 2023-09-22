def busca(setor:str,matriz:list)->list:
    """Dada uma matriz de funcionários e um setor dessa matriz, retorna a lista dos dados dos funcionários que trabalham nesse setor."""
    funcionarios=[]
    for dados_funcionarios in range(len(matriz)):
        if matriz[dados_funcionarios][2]==setor:
            list.remove(matriz[dados_funcionarios],setor)
            list.append(funcionarios,matriz[dados_funcionarios])
    return funcionarios