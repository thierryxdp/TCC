def colchao(medidas:list,H:int,L:int):
    list.sort(medidas)
    if L>H:
        if H>=medidas[0] and L>=medidas[1]:
            return True
        else:
            return False
    else:
        if L>=medidas[0] and H>=medidas[1]:
            return True
        else:
            return False