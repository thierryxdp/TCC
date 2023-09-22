def carros(numPessoas: int, capacidade: int = 4) -> int:
    '''
    Retorna número exato de carros necessários para uma viagem, dado o total de pessoas que vão
    viajar e a capacidade dos veículos
    '''
    if (numPessoas % capacidade) == 0:
        return numPessoas / capacidade
    else:
        return (numPessoas // capacidade) + 1