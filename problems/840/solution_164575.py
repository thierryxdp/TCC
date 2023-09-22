def bolos(A,B,C):
    "calcula a maior quantidade inteira de receita de bolo possível de acordo com a quantidade a de xícaras de farinha de trigo, quantidade b de ovos e quantidade c de colheres de sopa de leite"""
    return min((A//2),(B//3),(C//5))