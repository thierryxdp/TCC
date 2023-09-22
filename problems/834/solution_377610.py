def media_matriz(matriz):
    """funcao que dada uma matriz ela  retorna a media de todos os nuumeros da
    matriz.(com duas casas decimais). list->float."""
    nlin= []
    ncol= 0
    for matriz in matriz:
        for i in matriz:
            list.append(nlin,i)
            ncol +=1
    return round(sum(nlin)/ncol,2)