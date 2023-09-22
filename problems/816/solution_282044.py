def maiores(lista_numero,n):
    parametro=[[lista_numero],n]
    if parametro[1]< max(lista_numero):
        return [lista_numero>parametro[1]]
    if parametro[1]> max(lista_numero):
        return []