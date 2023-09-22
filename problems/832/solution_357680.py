def eh_quadrada(x):
    tamanho = len(x)
    for i in range(tamanho):
        linha = len(x[i])
        tamanho2 = tamanho - 1
        for j in range(tamanho2,0,-1):
            linha2 = len(x[j])
            if (tamanho == linha) and (tamanho == linha2):
                return True
            elif (tamanho ==0):
                return True
             elif (tamanho ==1) and (linha == 1):
                return False
            else:
                return False