def media_matriz(m):
    """Função que dada uma matriz(m) retorna a média de seus elementos com 2 casas decimais.
    list --> float"""
    soma = 0 
    divisor = len(m) * len(m[0])
    
    for lista in range(len(m)):
        soma += sum(m[lista])
        
    return round(soma / divisor, 2)