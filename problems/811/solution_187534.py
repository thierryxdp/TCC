def teste(a,b,c,h,l):
    colchao = a * b * c
    porta = h * l
    if colchao < porta:
        return True
    elif colchao > porta:
        return False
    else colchao == porta:
        return 'São do mesmo tamanho'