def insere(lista_numero,n):
    "Função que adiciona um inteiro n a lista de números em ordem crescente. list, int --> list"
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    "Função que retorna uma lista com os números maiores que n, dado uma lista em ordem crescente e o número n. list, int --> list"
    lista= insere(lista,n)
    ap=list.count(lista,n)
    i=list.index(lista,n)
    lista= lista[ap+i:]
    return lista
    
def acima_da_media(notas):
    "Função que retorna a lista com as notas acima da média da turma, dado as notas da turma como entrada. list --> list"
    media= sum(notas)/len(notas)
    acima= maiores(notas,media)
    return acima