def eh_quadrada(x):
    tamanho = len(x)
    tamanho2 = tamanho - 1
    for i in range(tamanho):
        linha = len(x[i])
        for j in range(tamanho2,0,-1):
            linha2 = len(x[j])
            if (tamanho == 1) and ( linha == 1):
                return True
            elif (tamanho == linha) and (tamanho2 == linha2):
                return True
            elif (tamanho == 1) and (linha > 1):
                return False
            else:
                return False