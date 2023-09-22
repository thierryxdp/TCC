def media_matriz(ls):
    qtd_num = 0
    soma = 0
    for listas in ls:
        soma += sum(listas)
        for numero in listas:
            qtd_num += 1
    return round(soma/qtd_num,2)