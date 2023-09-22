def conta_numero(numero,matriz):
    '''
    função que dado um inteiro e uma matriz de inteiros tamanho qualquer, conta quantas vezes o número
    pedido aparece dentro da matriz de inteiros
    int,list(list)--> int
    '''
    freq_num=0
    for linha in matriz:
        for num in linha:
            if num==numero:
                freq_num=freq_num+1

    return freq_num