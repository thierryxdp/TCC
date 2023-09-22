def maiores(L,n):
    """Função que retorna uma nova lista com os numeros maiores
    que n da lista dada  em ordem crescente.
    list, int->list"""
    list.append(L,n)
    list.sort(L)
    return L[L.index(n)+1:]

def acima_da_media(L):
    """Função que retorna uma lista com as notas
    que ficaram acima da média.
    list -> list"""
    if len(L)==1:
        return []
    else:
        media=sum(L)/len(L)
    	acima=maiores(L, media)
    return acima