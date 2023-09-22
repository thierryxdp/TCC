def carros(x,y=5):
    """função que dados o número de pessoas e (quando diferente do habitual de 5 lugares) a capacidade do carro, calcula e retorna a quantidade necessária de carros para o número de pessoas"""
    return ceil(float(x/y))