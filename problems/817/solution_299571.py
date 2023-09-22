def maiores(lista_numero, n):
    '''dada uma lista de inteiros de entrada e um número inteiro, 
    retorna outra lista, que contém todos os números da listaoriginal
    maiores que o número entrado;
    list, int -> list'''
    if n not in lista_numero:
        list.append(lista_numero, n)
    list.sort(lista_numero)
    posicao=list.index(lista_numero, n)
    posicao=posicao+1
    lista_nova=lista_numero[posicao:]
    return lista_nova
def acima_da_media(lista_notas):
    '''dada uma lista de inteiros de entrada e um número inteiro, 
    retorna outra lista, que contém todos os números da lista original
    maiores que a média dos números da lista;
    list -> list'''
    soma=sum(lista_notas)
    elementos=len(lista_notas)
    media=(soma/elementos)
    return maiores(lista_notas, media)