def maiores(lista,n):
    """Função que recebe uma lista e um numero inteiro e retorna todos os numeros da lista original maiores que n"""
    """lista, int->lista"""
    if n in lista:
        lista = sorted(lista)
        indexn=list.index(lista,n)
        return lista[(indexn+1):]
    else:
        list.append(lista,n)
        lista=sorted(lista)
        indexn=list.index(lista,n)
        return lista[(indexn+1):]
def acima_da_media(notas):
    """função que recebe uma lista com as notas de uma turma e retorna uma lista ordenada com as notas acima da média"""
    """lista->lista"""
    media=(sum(notas))/(len(notas))
    return maiores(notas, media)