def conta_numero(numero, matriz):
    '''
    Calcula a quantidade de vezes que determinado número aparece em uma matriz.
    int, list -> int

    Parameters:
    numero: Parâmetro numérico, do tipo inteiro (int);
    matriz: Parâmetro do tipo lista (list).
    
    Returns:
    A quantidade de aparições de determinado número em certa matriz.
    '''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    quantidade_numero = 0

    if type(numero) != int:
        return ("Utilize somente valores inteiros para o parâmetro numérico. Tente novamente!")

    for i in range(linhas):
        for j in range(colunas):
            if type(matriz[i][j]) != int:
                return ("Utilize somente valores inteiros para os elementos da matriz. Tente novamente!")
            
    for i in range(linhas):
        for j in range(colunas):
            if numero == matriz[i][j]:
                quantidade_numero = quantidade_numero + 1
                
    return quantidade_numero