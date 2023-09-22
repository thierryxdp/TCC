def bolos(a,b,c):
    """Calcula quantos bolos Joao consegue fazer dada a quantidade dos 
    ingradientes, xicaras de farinha: a, numero de ovos: b, colheres de
    sopa de leite: c """
    return min(a//2,b//3,c//5)