def num_carros():
    capaidade_carro = float(input("capacidade de pessoas no veiculo"))
    numero_pessoas = float(input("numero de pessoas"))
    return int(numero_pessoas/capaidade_carro)
print(num_carros())