def colchao(medidas,H,L):
    list.remove(medidas,max(medidas))
    if H>=max(medidas) and L>=min(medidas):
        return True
    else:
        return False