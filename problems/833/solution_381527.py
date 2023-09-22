def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    lista = str.split(matriz)
    ocorrencias = []
    
    for numeros in lista:
        qtd = str.count(numeros, numero)
        list.append(ocorrencias, qtd)
    return ocorrencias