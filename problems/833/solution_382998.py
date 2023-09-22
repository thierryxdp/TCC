def conta_numero(numero,matriz):
    """Dado um inteiro e uma matriz, retorna quantas vezes o numero aparece na matriz"""
    """entrada: int, lista(lista)
    saida: int"""
    
    lista = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                list.append(lista,numero)
                
    return len(lista)