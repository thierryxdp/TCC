def insere(lista_numero,n):
    '''Retorna a lista original em ordem crescente contendo n;
    list, int -> list'''
    lista_numero[0:0]=list(n)
    return list.sort(lista_numero)