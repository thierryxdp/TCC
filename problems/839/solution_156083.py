def carros(q, p=5):
    """Calcula e retorna a quantidade de carros para fazer uma viagem dado q(quantidade de pessoas) e p(pessoas em um carro). int->int"""
    if (q%p) == 0:
        return q//p
    else:
        return q//p + 1