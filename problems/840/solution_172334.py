def bolo(a, b, c):
    '''função que recebe o número de xícaras de farinha, 
    o número de ovos e de colheres de sopa de leite, e retorna a quantidade 
    máxima de bolos'''
    a = a//2
    b = b//3
    c = c//5
    return min(a, b, c)