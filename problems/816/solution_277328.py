def maiores(lista,n):
    """Essa função retorna quantos numeros da lista são maiores que o numeor n
    informado"""
    """list,int->list"""
    ordem=lista + [n]
    list.sort(ordem)
    return ordem[(list.index(ordem,n)+1):]