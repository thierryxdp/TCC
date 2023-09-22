def soma_h(N):
    '''função calcula somatório de frações com
    N termos onde cada fração tem denominador igual 
    a sua posição no somatório.
    int--> float'''

    lista_soma = [1]  #começa lista com elemento 1 porque o somatório começa com 1

    for numero in range(2, N+1):  #percorre todos os elementos do intervalo de 2 à N
        lista_soma.append((numero)**-1)  #adiciona em lista elementos que serão somados

    somatorio = sum(lista_soma)  #soma todos os elementos da lista

    return round(somatorio, 2)  #retorna o resultado do somatório