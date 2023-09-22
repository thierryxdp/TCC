def esp(a,b,c,h,l):
    colchao = [a*b*c]
    porta = [h*l]
    if colchao>porta:
        return False
    if colchao<=porta:
        return True