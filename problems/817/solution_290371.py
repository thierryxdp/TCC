def acima_da_media(notas):
    lista = []
    media = sum(notas) / len(notas)
    
    for elemento in notas:
        if elemento > media:
            lista.append(elemento)
    return lista