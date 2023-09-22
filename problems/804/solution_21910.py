def par(a,b,c,d):
    return (par(a),par(b),par(c),par(d))
def paridade(n):
    if n%2==0:
        return n
    else:
        return