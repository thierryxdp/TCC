def bolos(A,B,C):
    '''calcula e retorna o número máximo de bolos possíveis à ser feito(A= xícaras de farinha de trigo,B= números de ovos,C=colheres de sopa de leite'''
    return min(A//2,B//3,C//5)