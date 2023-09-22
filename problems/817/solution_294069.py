def maiores(lista, n):
    """Função que retorna uma lista que contenha todos os numeros da lista original maiores que o numero 'N'.
    lista, int - > list"""

    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)+1
    return lista[posicao:]

def media(lista):
    """Função que, dado uma lista, retorna a media das notas do aluno, junto a lista ordenada das notas acima da media.
    lista - > float, lista"""
    media_notas = sum(lista)/len(lista)
    return (media_notas, maiores(lista,media_notas))