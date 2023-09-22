def bolos(A=2,B=3,C=5):
    ''' Esta função calcula a quantidade de bolos que João
    pode fazer. '''
    qtd_farinha=A/2
    qtd_ovos=B/3
    qtd_leite=C/5
    return min(qtd_farinha,qtd_ovos,qtd_leite)//3