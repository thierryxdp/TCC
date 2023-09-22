def insere(lista_numero,n):
    
    """
    lista,int--->lista
    Foi colocado o valor n em lista para que fosse possivel a concatenacao
    entre ele e a lista_numero(a dada na entrada),logo em seguida foi aplicado
    o comando sort para que a ordem crescente fosse aplicada.
    """
    
    lista0=[n]
    lista1=(lista_numero+lista0)
    list.sort(lista1)
    
    return lista1