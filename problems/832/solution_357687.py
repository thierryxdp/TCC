def eh_quadrada(x):
    tamanho = len(x)
    if (tamanho>1):
        linha = len(x[0])
        if (tamanho == linha):
            return True
        else:
            return False
    else:
        if (tamanho ==0):
            return True
        else:
            return False