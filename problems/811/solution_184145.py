def colchao(medidas,h,l):
    """Calcula a área da porta e retorna se houve ou não a colisão,
    dados as dimenções do colchão."""
    return not(medidas > h and medidas > l)