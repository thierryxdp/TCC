def bolos(A,B,C):
    '''calcula e retorna a quantidade de bolos qie podem ser feitos
    com a quantidade de ingredientes dada
    entrada:int,int,int
    saida:int'''
    return min(A//2,B//3,C//5)