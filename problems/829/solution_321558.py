def soma_h(N):
    i = 1
    lista_de_fracoes = []
    while i <= N:
        H = 1/i
        lista_de_fracoes.append(H)
        i+= 1
    return round(sum(lista_de_fracoes),2)