def acima_da_media(numero):
    soma = sum(numero)
    x = len(numero)
    media = soma/x
    return maiores(numero,media)