def bolos(A,B,C):
    '''Função calcula e retorna a quantidade máxima de bolo que o usuário consegue fazer recebendo a=(nº de Xicarass de farinha) b=(nº de ovos) c(nº de colheres de açucar) disponíveis e retorna a quantidades de bolos possíveis de serem feitos'''
    return min (A//2, B//3, C//5)