def bolos(A,B,C):
    '''calcula a quantidade máxima de bolos que podem ser feitos dados A,
    B e C, que representam, respectivamente, a quantidade de xícaras de 
    farinha, ovos e colheres de sopa de leite'''
    return max(A//2,B//3,C//5)