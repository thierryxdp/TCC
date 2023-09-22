def media_matriz(M):
    media = 0
    soma = 0
    for a in M:
        for b in a:
            soma = soma + b
    media = 0 + (soma)/(len(M)*len(M[0]))  
    return round(media,2)