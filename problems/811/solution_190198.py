def colchao (dimensao, H, L):
    porta = [H, L]
    if dimensao[1] > porta[0] and dimensao[1] > porta[1]:
        return False
    else:
        return True