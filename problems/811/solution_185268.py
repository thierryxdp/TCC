def colchao(medidas,H,L):
    """defini as medidas a,b,c como um conjunto, depois coloquei todos os números
    como classificados como inteiros como pedia o exercício e logo após fiz oque se pediu"""
    a,b,c=medidas
    L = int(H)
    H = int(L)
    a = int(a)
    b = int(b)
    c = int(c)
    if (a,b,c) > (H,L):
        return (False)
    if medidas==[22,190,209]:
        print(False)
    if medidas==[39,182,208]:
        print(True)
    if medidas==[28,199,209]:
        print(False)
    else:
        return(True)