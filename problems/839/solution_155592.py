def carros(pessoas,capacidade=5):
    """Calcula a quantidade de carros para realizar uma viagem dados o número
    de pessoas e a capacidade dos veículos. Caso não seja informada será assumida
    a capacidade para 5 pessoas por veículo. Todos os veículos são iguais.
    int,int->int"""
    return pessoas//capacidade