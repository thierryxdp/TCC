def carros(num_pessoas,capacidade_carro):
    """
    função que ira retornar o numero de carros necessarios para uma viagem dados o numero de pessoas que irao.
    a capacidade do carro tem como argumento padrao 5. porem pode ser dado outro valor.
    int,int -> int
    """
    
    qtdcarros = num_pessoas / capacidade_carro
    return math.ceil(qtdcarros)