def colchao(medidas,h,l):
    maior_num = max(medidas)
    medidas.remove(maior_num)
    porta = [h,l]
    if2 = max(porta)
    if medidas[0] <= h or medidas[0] <= l:
        if medidas[1] <= if2:
            return 	True
        else:
            return False
    else:
        return False