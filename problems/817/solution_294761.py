def acima_da_media(notas):
    quantidade=len(notas)
    Sum=sum(notas)
    media=int((Sum/quantidade))+1
    notas_maiores=notas_maiores(notas,media)
    return notas_maiores