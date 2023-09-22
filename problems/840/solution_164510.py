"numero de bolos possiveis com a farinha"
def farinha(A):
    "pega-se o valor de farinha que tem-se e divide pelo valor necessário para fazer um bolo"
    return A//2

"numero de bolos possiveis com os ovos"
def ovos(B):
    "mesma coisa feita com a farinha"
    return B//3

"numero de bolos possiveis com o leite"
def leite(C):
    "mesma coisa feita com os dois outros ingredientes"
    return C//5

#desses valores pega-se o menor resultante das divisões inteiras e esse será o numero de bolos que pode-se fazer

def bolos(B):
    return ovos(B)//5