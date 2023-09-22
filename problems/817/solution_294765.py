def maiores(lista_numero,n):
    ordem= insere(lista_numero,n)
    return ordem[list.index(ordem,n)+1:]
def acima_da_media(notas):
    quantidade=len(notas)
    Sum=sum(notas)
    media=int((Sum/quantidade))+1
    notas_maiores=maiores(notas,media)
    return notas_maiores