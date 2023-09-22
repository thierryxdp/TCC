def insere(
    listaNumeroOrdenada: list[int],
    n: int
        ) -> list[int]:
    '''Insere n na sua respectiva posicao dentro da lista
       de numeros ordenada'''

    # [1, 4, 5, 6, 7, 8]  <-  n = 2
    # R. [1, 2, 4, 5, 6, 7, 8]

    # [10, 20, 40, 50, 60, 70, 80] <- n = 2
    # R. [2, 10, 20, 40, 50, 60, 70, 80]

    # Já temos um método de ordenação "list.sort"

    # Adicionando o elemento n na lista
    listaNumeroOrdenada.append(n)

    # Reordenando a lista, colocando "n" na sua respectiva
    # posicao
    listaNumeroOrdenada.sort()

    return listaNumeroOrdenada

def maiores(numeros,n):
     # Obtendo uma copia da lista numeros
    numerosCopia = numeros.copy()

##    # Adicionando o numero n na lista
    numerosCopia.append(n)
##
##    # Ordenando a lista para colocar n na sua respectiva
##    # posicao
    numerosCopia.sort()

    # Adicionando n na posicao respectiva
    numerosCopia = insere(numerosCopia, n)

    # Indentificar o indice onde foi colocado o numero n
    posicaoN = numerosCopia.index(n)

    # Obtendo os numeros maiores que n usando fatiamento
    numerosMaiores = numerosCopia[posicaoN+1:]

    # (Abrindo um "parenteses")
    if estritamente:
        # Removendo os numeros iguais a n, caso existam
        if n in numerosMaiores:
            # Contar quantos n's
            quantidade = numerosMaiores.count(n)

            # Eliminando os n's
            numerosMaiores = numerosMaiores[quantidade:]

    else:
        pass # Faça nada!
    
    return numerosMaiores