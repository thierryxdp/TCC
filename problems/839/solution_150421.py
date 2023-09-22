def carros(num_pessoas,capacidade_veiculo=5):
    """ Está função irá retornar o número exato de pessoas dentro de um carro.
Se o carro for considerado convencional, usar capacidade_veiculo=5.
Caso a capacidade do carro for diferente de 5, usar número na entrada da função"""
    return (num_pessoas//capacidade_veiculo) + 1