def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for elemento in range(colunas):
        if elemento == numero:
            contagem.append(numero)
    return elemento