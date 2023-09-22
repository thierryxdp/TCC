def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma//qntd
    a = media + 1
    if media in notas:
        return notas[a:]