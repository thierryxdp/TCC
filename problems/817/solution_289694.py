def acima_da_media(lista):
    """essa função retorna os elementos que estão acima da média de determinada lista;
    list->list"""
    x=sum(lista)/len(lista)
    return lista[x:]