def soma_h(N):
    lista_soma =[1]
    for num in range  (2, N+1):
        lista_soma.append((num)**-1)
    soma = sum(lista_soma)
    return round(soma, 2)