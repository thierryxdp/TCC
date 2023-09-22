def maiores(lista_numero,n):
    parametro=[[lista_numero],n]
    if parametro[1]< max(lista_numero):
        return all(max(lista_numero))
    if parametro[1]> max(lista_numero):
        return []