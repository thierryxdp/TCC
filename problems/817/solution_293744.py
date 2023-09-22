def acima_da_media(lista):
    '''Verifica se as notas são acima de 7 e, caso positivo, adiciona esses valores a uma lista ordenada
       list -> list'''
    media = int(sum(lista)/2)
    lista_aprovados = []
    for x in lista:
        if x >= media:
            lista_aprovados.append(x)
    return sorted(lista_aprovados)