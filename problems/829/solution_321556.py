def soma_h(N):
    i = 1
    lista_de_fracoes = []
    while i <= N:
        H = round(1/N, 2)
        lista_de_fracoes.append(H)
        i+= 1
    return sum(lista_de_fracoes)