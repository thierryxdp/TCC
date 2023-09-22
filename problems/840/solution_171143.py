def bolos(A,B,C):
    quant_de_bolos_por_xícaras_farinha_trigo = A//2
    quant_de_bolos_por_ovos = B//3
    quant_de_bolos_por_colheres_de_sopa_de_leite = C//5
    return min(quant_de_bolos_por_xícaras_farinha_trigo,quant_de_bolos_por_ovos,quant_de_bolos_por_colheres_de_sopa_de_leite)