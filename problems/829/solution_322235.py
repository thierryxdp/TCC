def soma_h(N):
    '''função calcula somatório de frações com
    N termos onde cada fração tem denominador igual 
    a sua posição no somatório.
    int--> float'''

    lista_soma = []
    contador = 0
    somatorio = 0

    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)

    for elemento in lista_soma:
        somatorio += lista_soma[contador]
        contador += 1

    return round(somatorio + 1, 2)