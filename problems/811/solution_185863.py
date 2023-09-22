def colchao(medidas,h,l):
    """a funcao calcula se um colchao com determinadas medidas ira passar pelas portas da casa de joa"""
    dim=medidas[:]
    dim.append(h)
    dim.append(l)
    dim.sort()
    altura=dim.count(h)-1
    altura=dim.index(h)+ altura
    largura=dim.count(l)-1
    largura=dim.index(l)+largura
    return((altura>0)and(largura>2))or((altura>1))