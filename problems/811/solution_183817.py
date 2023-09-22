def colchao(medidas,H,L):
    a,b,c=medidas
    porta=[H,L]
    if [a,b]<=porta:
        return True
    elif [b,c]<=porta:
        return True
    elif [a,c]<=porta:
        return True
    else:
        return False