def faltante(lista):
    """Função que, dada uma lista com N − 1 inteiros numerados de 1 a N, 
    descubra qual nº inteiro deste intervalo está faltando;
    list ->int"""
    contador = 0
    listaOrdenada = sorted(lista)

    while contador < len(lista):
        if contador + 1 == listaOrdenada[contador]:
            contador += 1

        else:
            return contador + 1

    return contador + 1