def carros(num_pessoas,capacidade_carro = 5):
    if capacidade_carro == 5:
        qtde = num_pessoas//capacidade_carro
        return qtde
    else:
        qtde1 = num_pessoas//capacidade_carro
        return qtde1+1