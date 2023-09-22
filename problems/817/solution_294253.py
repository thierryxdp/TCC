def acima_da_media(lista:list)->list:
    """ A funcao recebe uma lista de numeros inteiros. E retorna uma lista ordenada, dos numeros maiores que 5 """
    list.append(lista,5)
    list.sort(lista)
    indice_n = list.index(lista,5)
   
    return  lista[indice_n+1:]