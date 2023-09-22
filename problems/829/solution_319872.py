def soma_h(n):
    """Função para calcular o valor da séria H.
       Onde: "n" - é o numeros de termos da série H.
    int --> float """
    h = 0
    for i in range(1, n +1 ):
        parcela = 1 / i
        h += parcela
    return round(h, 2)