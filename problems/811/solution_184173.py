def colchao(medida,h,l):
    """Calcula a área da porta e retorna se houve ou não a colisão,
    dados as dimenções do colchão."""
    
    largura = medida[0]

    altura = medida[1]

    profundidade = medida[2]

    calculo = largura*altura*profundidade
    if (altura > h):
        return False
    else:
        return True