def total(compra):
    productos={'amaciante':4.99,'arroz':10.90,'biscoito':1.69,'cafe':6.98,'chocolate':3.79,'farinha':2.99}
    P=list(dict.keys(productos))
    V=list(dict.values(productos))
    r=len(compra)
    z=0
    x=[]
    lista=[]
    while z<r:
        c=P.index(compra[z])
        x.append((V[c]))
        z=z+1
    t=sum(x)
    return (round(t,2))