def media_matriz (matriz):
    """Função que recebe uma matriz não nula e retorna a media de todos os elementos da matriz;
    list -> float."""
    nova_lista= []
    for lista in matriz:
        for elemento in lista:
            nova_lista= nova_lista + [elemento,]
    return round (sum (nova_lista)/len(nova_lista), 2)