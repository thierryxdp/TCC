def bolos(A=2,B=3,C=5):
    ''' Esta função calcula a quantidade de bolos que João pode
    fazer. '''
    qtd_farinha=max(2,A)
    qtd_ovos=max(3,B)
    qtd_leite=max(5,C)
    return (qtd_farinha/2+qtd_ovos/3+qtd_leite/5)//3