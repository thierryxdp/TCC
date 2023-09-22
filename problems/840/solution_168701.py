def bolo(A,B,C):
    '''calcular a quantidade de bolos possíveis a serem feitos com a quantidade disponível de cada ingrediente sendo: A(quantidade de xícaras de farinha de trigo),
B (quantidade de ovos) e C (colheres de sopa de leite). Lembrando que na receita são necessárias respectivamente 2,3 e 5 de cada.'''
    return min (A//2,B//3,C//5)