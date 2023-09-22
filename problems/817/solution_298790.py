def maiores(lista,n):
    """dada uma lista de numeros inteiros e um número 
    inteiro n , ela retorna uma lista apenas com os numeros maiores 
    que n
    list, str-> list"""
    list.append(lista,n)
    list.sort(lista)
    indice_n=list.index(lista,n)
    indice=indice_n+1
    retornar=lista[indice:]
    return retornar
def acima_da_media(lista):
    """Dada uma lista com as notas dos
    alunos de uma turma, essa função retorna
    uma lista ordenada com as notas que ficaram acima 
    da média.
    list->list"""
    media=(sum(lista)/len(lista))
    listanova=maiores(lista,media)
    retornar=list.remove(listanova,media)
    return retornar