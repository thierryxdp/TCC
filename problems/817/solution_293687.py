def maiores(lista,n):
    """..."""
    l= lista
    a= [x for x in l if x > n]
    b= a.sort()
    return a
acima_da_media(lista):
    """determina as notas que ficaram acima da média;
    string, -> string"""
    media = sum(lista)/len(lista)
    return maiores(lista,media)