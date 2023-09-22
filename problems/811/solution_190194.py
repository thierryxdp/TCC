def colchao(medidas,H,L):
    """
    Código que calcula se determinado colchão com medidas 
    (a, b, c) passa em uma porta com valores H, L.
    :medidas---> List:
    :H---> Int:
    :L---> Int:
    :return bool:
    """
    L1=[L,H]
    L1.sort()
    l=L1[0]
    h=L1[1]
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if (l>=a and h>=b):
        return True
    else:
        return False