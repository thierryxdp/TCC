def faltante(pecas):
    '''list-> int'''
    x= len (pecas) + 1
    somatotal= x * (x + 1) // 2
    return somatotal - sum(pecas)