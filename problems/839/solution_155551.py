def carros(numPessoas: int, capacidade = 4: int) -> int:
    '''
    Retorna número exato de carros necessários para uma viagem, dado o total de pessoas que vão
    viajar e a capacidade dos veículos
    '''
    if (numPessoas % capacidade) == 0:
        return numPessoas / capacidade
    else:
        return (numPessoas // capacidade) + 1