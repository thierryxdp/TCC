def acima_da_media(lista):
    '''Verifica se as notas são acima de 7 e, caso positivo, adiciona esses valores a uma lista ordenada
       list -> list'''
    lista_aprovados = []
    for x in lista:
        if x => 6:
            lista_aprovados.append(x)
    return sorted(lista_aprovados)