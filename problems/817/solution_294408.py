def maiores(num_inteiros,n):
    list.append(num_inteiros,n)
    list.sort(num_inteiros)
    ps=list.index(num_inteiros,n)
    lista=num_inteiros[ps+1:]
    return lista


def acima_da_media(lista):
    media=sum(lista)
    m_maiores=maiores(lista,media)
    return m_maiores