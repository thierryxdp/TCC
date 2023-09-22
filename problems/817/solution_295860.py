def maiores(lista,n):
    """Dada uma lista de numeros unteuros e um numero inteiro n
    	retorna outra lista com os elementos maiores que n
        lista,int--->lista"""
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista [posicao+1:]

def acima_da_media(notas):
    """Dada uma lista de notas de uma turma, retorne uma lista
    ordenada com as notas que ficaram acima da media
    lista-->lista"""
    media=(sum(notas)/len(notas))
    if media in notas:
        list.remove(notas,media)
    return (maiores(notas,media))