def busca(setor, matriz):
    """Função que recebe uma matriz com quatro entradas, que são nome, registro, setor
    e telefone de um funcionario, respectivamente e um setor da empresa, retornado os 
    dados de todos os funcionarios daquele setor
    entrada: str, list(str)
    retorno:list(str)"""
    dados= []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(dados, matriz[i])
    for i in range(len(dados)):
        for j in range(len(dados[0])):
            if setor in dados[i,j]:
                list.remove(dados[i,j],setor)
    return dados