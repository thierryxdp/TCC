def faltante(lista):
    """A funcao retorna o numero inteiro que falta na lista numerada de 1 a n com
n - 1 numeros inteiros numerados, tendo tal lista como entrada. list --> int"""
    i = 0
    contador =  1
    while i < len(lista):
        if contador != lista[i]:
            return contador
        else:
            contador = contador + 1
            i = i + 1
    return contador