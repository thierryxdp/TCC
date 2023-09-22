import(math)
def carros(p,c=5):
    """Função que retorna o número de veículos necessários
    para um grupo de amigos realizar uma viagem, dados o 
    número de passageiros p e a capacidade c de pessoas
    nos veículos. Admitimos tambem o argumento defaut c=5
    para caso a capacidade do veículo não seja dada
    (consideramos um carro normal com capacidade para 5
    pessoas);
    int, int -> float"""
    return ceil(p/c)