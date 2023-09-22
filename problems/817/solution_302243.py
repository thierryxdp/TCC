def maiores(lista_numero, n):#funcao reutilizada do exercicio anterior
    '''funcao que retorna o numeros maiores que n contidos na lista_numero list,int->list'''
    if n in lista_numero:
        list.sort(lista_numero)
        lista1 = list.index(lista_numero,n)
        return lista_numero[lista1 + 1:]
    else:
        list.append(lista_numero,n)
        list.sort(lista_numero)
        lista1 = list.index(lista_numero,n)
        return lista_numero[lista1 + 1:]
def acima_da_media(lista_notas):
    '''funcao que retorna baseada na lista_notas outra lista ordenada com as notas que ficaram acima da media list->list'''
    media = (sum(lista_notas))/(len(lista_notas))
    return maiores(lista_notas,media)