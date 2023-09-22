def bolos (farinha,ovos,leite):
    'retorna a quantidade de bolos que podem ser feitos dadas as quantidades de cada ingrediente'
    unidades_farinha = farinha//2
    unidade_ovos = ovos//3
    unidade_leite = leite//5
    lista = [unidades_farinha,unidade_ovos,unidade_leite]
    return min(lista)