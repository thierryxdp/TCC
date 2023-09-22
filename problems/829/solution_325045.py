def soma_h(N):
    """funcao calcula somat ́orio de fracoes com
    N termos onde cada fra ̧c~ao tem denominador igual
    a sua posicao no somatorio.
    int--> float"""
    lista_soma = [1]
    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)
        somatorio = sum(lista_soma)
        return round(somatorio, 2)