def insere(lista_numero,n):
    """dada uma lista crescente de números, e um numero inteiro n de entrada
    insere o n na posição correta
    list, int --> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_Numero,N):
    """dada uma lista de numeros de entrada e um numero inteiro N, retorna
    uma lista que contém todos os numeros da lista original maior que N e 
    ordenados em ordem crscente
    list, int --> list"""
    insere(lista_Numero,N)
    indice_N=list.index(lista_Numero,N)
    return lista_Numero[indice_N+1:]

def acima_da_media(lista_Notas):
    """dada uma lista de notas de entrada, retorna uma lista
    com as quais ficaram acima da media aritmetica
    list --> list"""
    media_Aritmetica=sum(lista_Notas)/len(lista_Notas)
    notas_Acima=maiores(lista_Notas,media_Aritmetica)
    if media_Aritmetica in notas_Acima:
        list.remove(notas_Acima, media_Aritmetica)
    return notas_Acima