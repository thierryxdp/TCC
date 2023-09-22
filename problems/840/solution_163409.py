import math
def bolos(A,B,C):
    '''joão quer fazer bolo. A são xícaras de farinha; B são ovos; C são colheres de sopa de leite. a receita que possui 
    diz que precisa de 2 xícaras de farinha, 3 ovos e 5 colheres de leite para cada bolo. Ele não vai fazer um bolo cujo
    não tenha todos os ingredientes.'''
    A//2 B//3 C//5
    return math.min(A,B,C)