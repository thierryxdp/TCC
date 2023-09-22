def melhor_volta(matriz):
    """Função que verifica o tempo de cara corredor e retorna os 3 melhores tempos.
    Parametros: lista->tupla"""
    tupla = (1,2,3)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla