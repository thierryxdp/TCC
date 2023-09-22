def insere(lista_numero, n):
    '''Função que tendo como entrada uma lista de numeros crescentes e um 
    numero n, retorne a lista com n ordenado na sua posição correta
    list, int -> list'''
    list.extend(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero