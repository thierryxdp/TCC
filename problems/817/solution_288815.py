def acima_da_media(P1, P2, P3, peso1 = 4, peso2 = 6):
    media = (P1 * peso1 + max(P2, P3) * peso2) / (peso1 + peso2)
    return media