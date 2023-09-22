def acima_da_media(lista_nota):
    soma_das_notas=sum(lista_nota)
    qtd_de_notas = len(lista_nota)
    media_das_notas = soma_das_notas / qtd_de_notas
    return list(sorted(filter( lambda e: e >= n ,media_das_notas)))