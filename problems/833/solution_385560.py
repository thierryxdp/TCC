def conta_numero(numero,matriz):
    '''
    '''
    freq_num=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                freq_num=freq_num+1

    return freq_num