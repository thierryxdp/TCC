def acima_da_media(listaNotas):
    """Dada uma lista com todos os alunos, a função retorna uma lista
    ordenada com as notas que estão acima da média.
    Parametros de Entradas:list
    Retorna: list"""

    auxiliar= len(listaNotas)
    soma= sum(listaNotas)
    auxiliar= soma//auxiliar

    return maiores(listaNotas,auxiliar)

def maiores(lista,n):
    
    list.append(lista,n)
    list.sort(lista)

    auxiliar= list.index(lista,n)
    listaSaida= lista[auxiliar+1:]

    return listaSaida