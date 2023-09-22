def acima_da_media(lista):
    """ essa função irá calcular a média das notas dos alunos e irá retornar as ntoas que ficaram acima da média
    entrada -> lista
    saida -> lista """
    média = sum(lista)/ len(lista)
    list.append(lista, média)
    list.sort(lista)
    numero = list.index(lista, média)
    del lista[0:numero+1]
    return lista