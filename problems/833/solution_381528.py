def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    ocorrencias = []
    
    for numeros in matriz:
        qtd = str.count(numeros, numero)
        list.append(ocorrencias, qtd)
    return ocorrencias