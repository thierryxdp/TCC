def bolos(A, B, C):
    '''retorna a quatidade maxima de bolos dados
    os ingredientes A(xicara farinha), B(ovos) e
    C(colheres leite) em inteiros e tendo como 
    base para 1 bolo(A=2, B=3, C=5).'''
    return min(A//2, B//3, C//5)