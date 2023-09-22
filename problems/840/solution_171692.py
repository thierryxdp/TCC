def bolos (farinha,ovos,leite):
    unidades_farinha = farinha//2
    unidade_ovos = ovos//3
    unidade_leite = leite//5
    lista = [unidades_farinha,unidade_ovos,unidade_leite]
    return min(lista)