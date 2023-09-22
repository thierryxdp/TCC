def bolos(farinha, ovos, leite):

    divisãoFarinha = farinha//2
    divisãoovos = ovos//3
    divisãoleite = leite//5
    result = min(divisãoFarinha, divisãoovos, divisãoleite)
    return result