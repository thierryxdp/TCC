def carros (p,l=5):
    """Essa função calcula a quantidade de carros que
    serão utilizados para a viagem de um determinada 
    quantidade de pessoas 'p', onde 'l' é a quantidade de 
    lugares no carro."""
    import math
    return (math.ceil(p/l))