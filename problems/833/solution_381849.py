def conta_numero (numero, matriz):
    """Função que, dado um número inteiro e uma matriz de inteiros de tamanho qualquer, retorna quantas vezes aquele número aparece na matriz
    entrada: int, list
    saída: int"""
    
    quantidade = 0
    
    for linha in matriz:
        for coluna in linha:
            if numero == coluna:
                quantidade = quantidade + 1
                
    return quantidade