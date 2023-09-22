import math
def bolos(A,B,C):
    '''calcula o numero de bolos que 
       serao possivel fazer dadas as 
       quantidade de xicaras de 
       farinha de trigo(A), ovos(B)
       e colheres de sopa de leite(C)
       int, int, int -> int'''
    return min((A//2),(B//3),(C//5))