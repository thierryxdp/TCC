def acima_da_media(lista:list)->list:
    """ A funcao recebe uma lista de numeros inteiros. E retorna uma lista ordenada, dos numeros maiores que 5 """
    soma_das_notas = sum(lista)
    quantidade_numeros = len(lista)
    media = soma_das_notas / quantidade_numeros
    return media