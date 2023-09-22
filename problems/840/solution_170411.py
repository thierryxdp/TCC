def farinha(f):
    return f//2
def ovos(o):
    return o//3
def leite(l):
    return l//5
def bolos(f,o,l):
    '''calcula quantos bolos podem ser feitos com o número de ingredientes disponíveis'''
    return min(farinha(f),ovos(o),leite(l))