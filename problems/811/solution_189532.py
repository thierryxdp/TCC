def colchao(medidas,h,l):
    """Função que tem como entrada as medidas da cama e da porta, e retorna true se o colchao passa pela porta e false para caso ao contrário"""
    medidas=[A,B,C]
    if medidas[0]*medidas[1]>h*l:
        return False
    else:
        return True