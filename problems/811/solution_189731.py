def colchao (medidas, H,L):
    ' Função que retorna false ou true para o cálculo das medidas do colchão e o vão da porta'
    'lista ->lista'
    if medidas [1] <= H and medidas [1] <= L:
        return True
    else:
        return False