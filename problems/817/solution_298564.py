def maiores(lista,n):
    """ Função que dada uma lista, retorna outra lista contendo todos os números da lista original maiores que n, ordenados em ordem crescente 
    list,int -> list """
  
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[(a+1):]
def acima_da_media(lista):
    """ Função que dada uma lista com as notas de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média
    list -> list """
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(0,media)
    lista.sort()    
    indexdamedia = list.index(lista,media)
    listaF =lista[indexdamedia+1:]
    if listaF[0]==media:
        listaF.remove(media)
    return listaF