def melhor_volta(matriz):
    """Função que identifica o menor tempo de uma matriz
    e retorna uma tupla contendo as informações: de foi o menor tempo
    qual foi esse menor tempo e em que volta faz o n=menor tempo
    list -> tuple"""
    quem = 0
    quando = 0
    minimo = matriz[0][0]+1
    for i in matriz:
        menor = min(i)
        if menor < minimo:
            minimo = menor
            quem = matriz.index(i)+1
            quando = i.index(menor)+1
    return (quem, minimo, quando)