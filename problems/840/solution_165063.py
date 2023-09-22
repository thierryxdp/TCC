def bolos(a, b, c):
    """"determina qual a quantidade máxima de bolos que é possível
    fazer utilizando "a" xícaras de farinha de trigo, "b" ovos e "c"
    colheres de sopa de leite, sendo que a receita para fazer 1 bolo
    é 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de
    leite"""
    
    razoes_ingredientes = []
    razao_farinha = (a//2)
    razoes_ingredientes.append(razao_farinha)
    razao_ovos = (b//3)
    razoes_ingredientes.append(razao_ovos)
    razao_leite = (c//5)
    razoes_ingredientes.append(razao_leite)
    
    return min(razoes_ingredientes)