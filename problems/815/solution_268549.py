def insere(lista_numero, n):
    '''Dados uma lista de numeros e um numero inteiro, a função retorna
       a lista acrescida do numero e em ordem crescente.
       list, int -> list
       parametros:
       lista_numero: lista numerica a ser digitada
       n: numero inteiro a ser digitado'''
    if n in lista_numero:
        return lista_numero.sort
    else:
        lista = list.insert(lista_numero, len(lista_numero), n)
        listaord = lista.sort
        return listaord