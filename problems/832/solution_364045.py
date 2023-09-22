def eh_quadrada(num):
    linha = 0
    coluna = 0
    for i in range(len(num)):
        linha += 1
        for j in range(len(num)):
            if linha == coluna:
                return True
            else:
                return False
    else:
        return True