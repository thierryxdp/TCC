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
            list.remove(dados[i],setor)
    return dados