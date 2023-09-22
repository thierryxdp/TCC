def conta_numero (numero, matriz):
    """funçao que recebe um numero inteiro e uma matriz no formato lista de listas e retorna quantas vezes o numero aparece na matriz;
    entrada: int, list;
    saida: int."""
    
    soma = 0
                         
    for linha in matriz:
        for coluna in linha :
            if matriz[linha][coluna] == numero:
                soma = soma + 1
    return soma