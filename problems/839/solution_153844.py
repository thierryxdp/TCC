def carros(P,C=5):
    """Calcula a quantidade máxima de carros necessários para
    a viagem dado a quantidade de pessoas(P) e a capacidade(C)
    máxima dos carros"""
    return (P//C)+(ceil((P%C)/C))