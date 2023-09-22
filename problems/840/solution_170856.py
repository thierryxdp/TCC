def bolo(A,B,C):
    '''calcula e retorna a quantidade máxima de bolos que podem ser feitos com quantidades A ,B e C de ingredientes'''
    '''float,float,float->int'''
    qtd = ((A//2),(B//3),(C//5))
    limite = min(qtd)
    return limite