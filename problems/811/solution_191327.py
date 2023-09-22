def passa_colchao(colchao,H,L):
    """
    """
    a = colchao[0]
    b = colchao[1]
    c = colchao[2]
    colchao = [a,b,c]
    if (b<=H) and (a<=L):
        return "True"
    else:
        return "False"