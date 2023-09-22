import math
def xicaras(A):
    '''calcula quantas xícaras de farinha podem ser usadas em um bolo que necessita de duas'''
    return A//2
def ovos(B):
    ''' calcula quantos ovos podem ser usados para se fazer um bolo que necessita de três'''
    return B//3
def leite(C):
    '''calcula quantas colheres de leite podem ser usadas para se fazer um bolo que necessita de 5'''
    return C//5
def bolos (A, B, C):
    '''função que calcula quantos bolos podem ser feitos levando em conta quanto ingrediente se tem e quanto é necessário para fazer um bolo'''
    return min(xicaras(A), ovos(B), leite(C))