def media_matriz(matriz):
    """Inicia com 3 variáveis: uma pra soma(s), outra para
    média(m) e outra para contagem de elementos (c).
    Varre as linhas e depois varre as colunas, analisando
    cada elemento. Ele soma todos os elementos em s e soma
    um elemento em k. Depois calcula a média e arredonda."""
	s = 0; m = 0; c = 0
    for i in matriz:
        for j in i:
            s += j
            c += 1
    m = s/c; m = round(m, 2)
    return m