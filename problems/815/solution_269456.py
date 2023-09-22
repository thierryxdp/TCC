def insere(lista_numero, n):
    '''Função que tendo como entrada uma lista de numeros crescentes e um 
    numero n, retorne a lista com n ordenado na sua posição correta
    list, int -> list'''
    list.sort(lista_numero)
    if n in lista_numero== True:
        a= list.index(lista_numero,n)
        return list.insert(lista_numero,a,n)