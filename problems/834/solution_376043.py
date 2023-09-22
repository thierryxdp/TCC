def media_matriz (matriz):
    """Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz, com duas casas decimais de precisão
    entrada: list
    saída: float"""
    
    soma = 0
    quantidade = 0
    
    for linha in matriz:
        for coluna in linha:
            soma = soma + coluna
            quantidade = quantidade + 1
            
    return soma/quantidade