import math
def bolinho(a,b,c):
    """ ao informar a quantidade de farinha que possui, ovo 
    colher de leite - respectivamente a,b,c - a funcao retor
    nara a quantidade de bolinhos que sera possivel fazer.
    int,int,int -> int """
    return min(a//2,b//3,c//5)