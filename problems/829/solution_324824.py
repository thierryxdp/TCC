def soma_h(n):
    "função cálcula a soma de frações com N termos onde cada fração tem um denominador igual a sua posição na soma"
    h = 0
    contagem = 0
    limit = n + 1
    while contagem < limit:
        if contagem > 0:
            h += 1 / contagem
        contagem += 1
    h = round(h, 2)
    return h