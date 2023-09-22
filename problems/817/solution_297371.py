def insere(lista_numero,n):
    nova_lista_numero=lista_numero+[n]
    list.sort(nova_lista_numero)
    return nova_lista_numero

def maiores(lista_numero,n):
    indice_do_n=list.index(insere(lista_numero,n),n)
    return insere(lista_numero,n)[indice_do_n+1:]

def acima_da_media(lista_de_notas):
    """funcao que retorna uma lista ordenada com as notas acima da media;
    list de int -> list de int"""
    media=sum(lista_de_notas)/len(lista_de_notas)
    return maiores(lista_de_notas,media)