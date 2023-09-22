def carros(pessoas, capacidade_veiculo):
    if (capacidade_veiculo == 5) and (capacidade_veiculo > 0):
        return pessoas // 5
    else:
        return pessoas // capacidade_veiculo