def carros(numero_de_pessoas, capacidade_do_veiculo=5):
    return capacidade_do_veiculo - (numero_de_pessoas%capacidade_do_veiculo)