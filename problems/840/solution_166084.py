def bolos(a, b, c):
    """"determina qual a quantidade máxima de bolos que é possível
    fazer utilizando "a" xícaras de farinha de trigo, "b" ovos e "c"
    colheres de sopa de leite, sendo que a receita para fazer 1 bolo
    é 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de
    leite;
    int, int, int -> int"""
    
    razao_farinha = int(a/2)
    razao_ovos = int(b/3)
    razao_leite = int(c/5)
    
    return min(razao_farinha, razao_ovos, razao_leite)