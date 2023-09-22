def maiores(lista,numero):
    """Função que, dada uma lista e um número, retorna outra lista, porém, escolhendo somente
os números da lista original maiores que N; Entrada->List e int, Saída->List"""
    list.append(lista,numero)
    list.sort(lista)
    x=list.index(lista,numero)
    return lista[x+1:]

def acima_da_media(lista):
    """Função que retorna uma lista ordenada com notas que ficaram acima da média,
dado um conjunto de notas(lista); Entrada->List e int, Saída->List"""
    s=sum(lista)
    d=len(lista)
    numero=s//d-1
    maiores(lista,numero)
    return lista[numero:]