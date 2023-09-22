def bolos(xicaras, ovos, colheres_leite):
    quantidades = [round(xicaras/2 - 0.5), round(ovos/3 - 0.5), round(colheres_leite/5 - 0.5)]
    quantidades.sort()
    return quantidades[0]