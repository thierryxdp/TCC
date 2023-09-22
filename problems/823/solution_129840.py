def faltante(lista):
    """A funcao retorna o numero inteiro que falta na lista numerada de 1 a n com
n - 1 numeros inteiros numerados. list --> int"""
    i = 0
    lista.sort()
    contador =  list(range(lista[0],(len(lista)+1)+1))
    while i < len(lista):
        if contador[i] in lista:
            return contador[i]
        else:
            i = i + 1