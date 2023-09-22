def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    ocorrencias = ''
    
    for i in len(matriz):
        qtd = 0
        for j in i:
            if j == numero:
                qtd = qtd + 1
        list.append(ocorrencias, qtd)
    return ocorrencias