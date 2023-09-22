def insere(lista_numero, n):
    #Função que adiciona um número na lista e retorna a lista em ordem crescente
    #[], int -> []
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero