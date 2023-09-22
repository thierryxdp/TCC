def bolos(A=2,B=3,C=5):
    ''' Esta função calcula a quantidade de bolos que João
    pode fazer.
    int, int, int -> int '''
    qtd_farinha=A
    qtd_ovos=B
    qtd_leite=C
    return min(qtd_farinha/2+qtd_ovos/3+qtd_leite/5)//3