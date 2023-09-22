def insere(lista_numero,n):
    '''funcao que apos inserir uma lista e um numero n, ira retornar a lista inicial mais o numero n na sua posicao correta quando organizado crescentemente
    list, int -> list''' 
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero