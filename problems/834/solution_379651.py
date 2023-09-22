def media_matriz(ls):
    """Essa função serve para calcular a média de todos os números da
    matriz (ls)
    list->float"""
    qtd_num = 0
    soma = 0
    for listas in ls:
        soma += sum(listas)
        for numero in listas:
            qtd_num += 1
    return round(soma/qtd_num,2)

#media_matriz([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]) == 9.5
#media_matriz([[1,1],[1,1]]) == 1.0
#media_matriz([[555,666],[777,888]]) == 721.5