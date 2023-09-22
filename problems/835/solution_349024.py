def melhor_volta(m):
    """função que retorna a melhor volta da prova, com qual tempo e em que volta,
    através da matriz de entrada m;
    Entrada: list
    Saída: tuple"""
    final = []
    resposta = ()
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            menortempo = min(m[i])
            list.append(final,menortempo)
            resultado = min(final)
            if m[i][j] == resultado:
                posicao = j + 1
                volta = i +1
    return (volta, resultado, posicao)