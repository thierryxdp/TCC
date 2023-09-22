def maiores(lista_numeros, n):
    nova_lista = []
    for x in lista_numeros:
        if(x > n):
            nova_lista.append(x)
    
    nova_lista.sort()
    return nova_lista

def acima_da_media(lista_notas, media):
    lista_acima = maiores(lista_notas, media)
    return lista_acima