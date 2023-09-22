def colchao(medidas,H,L):
    list.sort(medidas)
    porta = [H,L]
    list.sort(porta)
    if not medidas[0] <= porta[0]:
        return False   
    if not medidas[1] <= porta[1]:
        return False
    else:
        return True