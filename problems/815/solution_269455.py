def insere(lista_numero, n):
    '''Função que tendo como entrada uma lista de numeros crescentes e um 
    numero n, retorne a lista com n ordenado na sua posição correta
    list, int -> list'''
    list.sort(lista_numeros)
    if n in lista_numeros== True:
        a= list.index(lista_numeros,n)
        return list.insert(lista_numeros,a,n)