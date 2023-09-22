def bolos(xicaras, ovos, colheres_leite):
    quantidades = [round(xicaras/2 - 0.4), round(ovos/3 - 0.4), round(colheres_leite/5 - 0.4)]
    quantidades.sort()
    return quantidades[0]