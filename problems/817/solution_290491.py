def acima_da_media(notas):
    """Funcao que dada uma lista retorna as notas acima da media"""
    media=sum(notas)/len(notas)
    list.sort(notas)
    lista_maiores=(notas,media)
    return lista_maiores