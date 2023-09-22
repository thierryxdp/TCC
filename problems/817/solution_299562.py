def maiores(lista_numero, n):
    '''dada uma lista de inteiros de entrada e um número inteiro, 
    retorna outra lista, que contém todos os números da list original
    maiores que o número entrado;
    list, int -> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    posicao=list.index(lista_numero, n)
    posicao=posicao+1
    lista_nova=lista_numero[posicao:]
    return lista_nova
def acima_da_media(lista_notas):
    soma=sum(lista_notas)
    elementos=len(lista_notas)
    media=soma//elementos
    return maiores(lista_notas, media)