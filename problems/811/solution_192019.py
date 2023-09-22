def colchao(medidas:list,H:int,L:int):
    list.sort(medidas)
    if int(medidas[0]**2+medidas[1]**2)<=int(H**2+L**2):
        return True
    else:
        return False