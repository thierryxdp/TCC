def media_matriz(matriz):
    '''
    Inicia 3 variáveis: uma pra soma (s), outra para 
    média (m) e outra para contagem de elementos (k).
    Varre as linhas e depois varre as colunas, analisando
	cada elemento. Ele soma todos os elementos em s e soma
    um elemento em k. Depois efetua a média e arredonda.
    '''
    s = 0; m = 0; k = 0
    for i in matriz:
        for j in i:
            s += j
            k += 1
	m = s/k; m = round(m, 2)
    return m