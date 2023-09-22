def bolos (A,B,C):
    """calcula e retorna quantos bolos são possíveis fazer, dadas as quantidade de 
    xícaras de farinha de trigo,ovos e colheres de sopa de leite,respectivamente"""
    return min((A//2),(B//3),(C//5))