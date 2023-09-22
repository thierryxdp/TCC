def maiores(lista, numero):
    lista.append(numero)
    if max(lista) == numero:
        return []
    else:
        lista_decrescente = sorted(lista, reverse=True)
        index_n = lista_decrescente.index(numero)
        return sorted(lista_decrescente[:index_n])
    
def acimda_da_media(x):
    media = sum(x)/(1.0*len(x))
    aprovados = maiores(x,media)
    return aprovados