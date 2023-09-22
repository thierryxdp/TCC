def colchao (medidas:list, H:int, L:int)->bool:
    '''recebe a medida do colchão, L e H correspondente respectivamente a largura da porta e a
    altura, retornando true se o colchao passar pela porta e false se não'''
    compc = medidas[1]
    if compac > H and compac>L:
        return False
    elif compac <= L or compac <= L:
        return True