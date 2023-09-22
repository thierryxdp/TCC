def acima_da_media(lista):
    """ essa função irá calcular a média das notas dos alunos e irá retornar as ntoas que ficaram acima da média
    entrada -> lista
    saida -> lista """
    media = sum(lista)// len(lista)
    list.append(lista,media)
    list.sort(lista)
    numero = list.index(lista,media)
    del lista[0:numero+2]
    return lista