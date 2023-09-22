def bolos(A=2,B=3,C=5):
    ''' Esta função calcula a quantidade de bolos que João
    pode fazer.
    int, int, int -> int '''
    qtd_farinha=A
    qtd_ovos=B
    qtd_leite=C
    return min(qtd_farinha,qtd_ovos,qtd_leite)//3