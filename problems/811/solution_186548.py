def colchao (medidas, H,L):
    ' Função que retorna false ou true para o cálculo das medidas do colchão e o vão da porta'
    'lista ->lista'
    if medidas [L] <= H:
        return True
    if medidas [L] <= L:
        return True
    else:
        return False