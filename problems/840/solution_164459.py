#2 xícaras de farinha de trigo
#3 ovos
#5 colheres de sopa de leite
#A=xícaras de farinha de trigo
#B=ovos
#C=colheres de sopa de leite
def bolos(A,B,C):
    '''função que dados os parametros A=xícaras de farinha de trigo, B=ovos, C=colheres de sopa de leite retorna a quantidade máxima de bolos que é possível fazer; int, int, int -> int'''   
    farinha=A//2
    ovos=B//3
    colheres=C//5
    return min(farinha,ovos,colheres)