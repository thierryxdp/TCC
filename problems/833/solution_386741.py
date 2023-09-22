def conta_numero(numero,matriz):
    """Função que dado um numero e uma matrix, retorna quantas vezes esse número aparece na matrix. Entrada -> Int and Matrix; Saída -> int"""
    contador = 0
    if len(matriz)==0:
        return contador
    elif len(matriz)!=0:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                elemento=matriz[i][j]
                if elemento == numero:
                    contador+=1
    return contador