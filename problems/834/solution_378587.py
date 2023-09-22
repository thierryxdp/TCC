def media_matriz(matriz):
    """Retorna a média de todos os numeros de uma dada matriz
, com  exatidão de duas casas decimais; list->float"""
    c=0
    s=0
    for i in matriz:
        c=c+len(i)
        s=s+sum(i)
    return round(s/c,2)