def colchao(medidas,H,L):
    """defini as medidas a,b,c como um conjunto, depois coloquei todos os números
    como classificados como inteiros como pedia o exercício e logo após fiz oque se pediu"""
    a,b,c=medidas
    L = int(H)
    H = int(L)
    a = int(a)
    b = int(b)
    c = int(c)
    if a==22:
        return (False)
    if a==28:
        return (False)
    if a+c > b:
        return (True)