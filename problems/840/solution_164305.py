def bolos(A,B,C):
    qtd_xicaras = A//2
    qtd_ovos = B//3
    qtd_leite = C//5
    qtd_bolos = min(qtd_xicaras,qtd_ovos,qtd_leite)
    return qtd_bolos