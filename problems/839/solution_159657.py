def carros(pessoas,capacidade=5):
    import math
    '''
    função que calcula o numero de carros necessarios para uma viagem dados o numero de pessoa
    e a capacidade do veiculo no caso de um veiculo com mais ou menos de 5 lugares
    int, int -> int
    '''
    return (ceil((pessoas)/(capacidade)))