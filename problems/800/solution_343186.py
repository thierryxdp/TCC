def total(lista,cardapio):
    """funcao que recebe """
    dispo=[]
    for p in lista:
        if dict.get(cardapio,p,0)!=0:
            list.append(dispo,dict.get(cardapio,p))
    return round(sum(dispo),2)