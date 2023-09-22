def colchao([A,B,C],h,l):
    """Função que tem como entrada as medidas da cama e da porta, e retorna true se o colchao passa pela porta e false para caso ao contrário"""
    lista=[A,B,C]
    if lista[0]*lista[1]>h*l:
        return False
    else:
        return True