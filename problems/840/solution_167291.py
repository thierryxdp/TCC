def bolos (farinha, ovos, leite):
    """Retorna o número máximo de bolos que João consegue fazer, dados: o número de 'xícaras de farinha de trigo', a quantidade de ovos e o número de 'colheres de sopa de leite' que ele possui em casa."""
    return round (min (farinha/2, ovos/3, leite/5))