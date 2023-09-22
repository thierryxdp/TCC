def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, a função conta e retorna para o usuário o número de
    vezes que o inteiro de entrada aparece na matriz.
    int, matriz -> int"""
    
    contador = 0
    for i in range(len(matriz)):
        
        for j in range(len(m[0])):
            candidato = matriz[i][j]
            
            if candidato == numero:
                contador +=1