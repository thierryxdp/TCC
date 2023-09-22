def conta_numero(numero: int, matriz: list) -> int:
    
    resultado = 0
    
    for i in matriz:
        for j in matriz:
            if numero == matriz[i][j]:
                resultado += 1