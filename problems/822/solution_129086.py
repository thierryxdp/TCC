def repetidos(ls):
    qtd_repetidos = 0
    for i in range(1,len(ls)):
        if(ls[i-1] == ls[i]):
            qtd_repetidos += 1
    return qtd_repetidos