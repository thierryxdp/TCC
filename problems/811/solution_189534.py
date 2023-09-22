def colchao([A,B,C],h,l):
    """Função que tem como entrada as medidas da cama e da porta, e retorna true se o colchao passa pela porta e false para caso ao contrário"""
    medidas=[A,B,C]
    if A*B>h*l:
        return False
    else:
        return True