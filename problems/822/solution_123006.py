def repetidos(lista):
    """Função recebe um lista e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
       Parametros: list -> int"""
    contador = 0
    vezes = 0
    anterior = 0
    atual = 0 
    while contador < len(lista):
        if contador == 0:
            atual = lista[contador]
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes = vezes + 1
        anterior = atual
        contador = contador + 1
    return vezes