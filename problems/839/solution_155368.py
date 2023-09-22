def carros (passageiros, carro=5):
    '''calcula a quantindade de carros necessaria para transportar uma quantidade de pessoas, considerando que um carro geralmente tem apenas 5 vagas (argumento defoult), podendo variar essa capacidade do veiculo''' 
    return int(passageiros/carro)