carros(npessoas, capacidade=5):
    """Esta funcao calcula quantos carros serao necessarios para transportar
    n pessoas, sabendo n e a capacidade do carro. Caso a capacidade nao seja
    preenchida, usaremos capacidade = 5."""
    return npessoas//capacidade