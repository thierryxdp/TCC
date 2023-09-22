def carros(pessoas,veiculo=5):
    if pessoas%veiculo >0:
        return pessoas//veiculos + 1
    else:
        return pessoas//veiculos