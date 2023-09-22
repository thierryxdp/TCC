def bolos (A,B,C):
    '''calcula a quantidade maxima de bolos que se pode fazer a partir
    dos ingredientes iniciais,A=xicara de farinha de trigo, B=ovos, 
    C= colheres de sopa de leite'''
    return min(A/2,B/3,C/5)