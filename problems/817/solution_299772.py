def maiores(
    numeros: list[int],
    n: int,
    estritamente: bool = False
        ) -> list[int]:
    '''Retorna uma lista com todos os numeros da lista
       de entrada que são maiores que n'''

    # Obtendo uma copia da lista numeros
    numerosCopia = numeros.copy()

##    # Adicionando o numero n na lista
##    numerosCopia.append(n)
##
##    # Ordenando a lista para colocar n na sua respectiva
##    # posicao
##    numerosCopia.sort()

    # Adicionando n na posicao respectiva
 

    # Indentificar o indice onde foi colocado o numero n
    posicaoN = numerosCopia.index(n)

    # Obtendo os numeros maiores que n usando fatiamento
    numerosMaiores = numerosCopia[posicaoN+1:]

    # (Abrindo um "parenteses")
        # Removendo os numeros iguais a n, caso existam
    if n in numerosMaiores:
            # Contar quantos n's
            quantidade = numerosMaiores.count(n)

            # Eliminando os n's
            numerosMaiores = numerosMaiores[quantidade:]

    else:
        pass # Faça nada!
    
    return numerosMaiores

def acima_da_media(
    notas: list[float]
        ) -> list[float]:
    '''Retorna as notas que estão acima da média'''

    # Calcular a média das notas
    media = sum(notas)/len(notas)

    # Recolhendo as notas estritamente maiores que a media
    acimaDaMedia = maiores(notas, media,True)

    return acimaDaMedia  # , media