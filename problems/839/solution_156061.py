def carros(pessoas,veiculo=5):
    if pessoas%veiculo >0:
        return pessoas//veiculo + 1
    else:
        return pessoas//veiculo