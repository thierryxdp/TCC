def media_matriz(m):
    
    """
    A média é a soma dos valores divididos pela quantidade. A quantidade
    é a multiplicacao entre o tamanho das linhas e das colunas, enquanto a
    soma vem de uma variável vazia que a cada leitura é feita a soma, até
    que a matriz se acabe e a operação seja realizada por completo
    """
    tamanho=len(m)*len(m[0])
    soma=0
    
    for linha in m:
        for posicao in linha:
            soma+=posicao
            
    return round(soma/tamanho,2)