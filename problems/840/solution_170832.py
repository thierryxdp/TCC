def xicaras(a):
    'Número de xícaras inseridas / Quantidade necessária na receita (2)'
    return a//2

def ovos(b):
    'Número de ovos inseridos / Quantidade necessária na receita (3)'
    return b//3

def colheres(c):
    'Número de colheres de sopa inseridass / Quantidade necessária na receita (5)'
    return c//5

def bolos(a,b,c):
    """Receita
    2 Xícaras de Farinha
    3 Ovos
    5 Colheres de Sopa de Leite"""
    return min(xicaras(a),ovos(b),colheres(c))

"""A função bolo retorna sempre o mínimo de bolos que podem ser feitos entre os 3 ingredientes.
Ex: 4 Xícaras / 2 = 2; 9 Ovos / 3 = 3; Colheres de leite = 15 / 5 = 3.
Mínimo entre (2, 3, 3) = 2), logo podem ser feitas duas receitas com 4 Xícaras de farinha de trigo, 9 Ovos e 15 colheres de sopa de leite """