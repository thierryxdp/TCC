def media_matriz(lista):
    for elemento in lista:
        for matriz in elemento:
            soma=sum(elemento)
            quantidade=len(elemento)
        media=soma/quantidade
    return round(media,2)