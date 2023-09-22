def acima_da_media(lista:list)->list:
    """ A funcao recebe uma lista de numeros inteiros. E retorna uma lista ordenada, dos numeros maiores que a media desses numeros"""
    soma_das_notas = sum(lista)
    quantidade_numeros = len(lista)
    media = soma_das_notas / quantidade_numeros
    list.append(lista,media)
    
    return lista