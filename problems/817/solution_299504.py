def acima_da_media(L):
    """Função que retorna uma lista com as notas
    que ficaram acima da média.
    list -> list"""
    media=sum(L)/(float(len(L))) 
    acima=maiores(L, media)
    return acima