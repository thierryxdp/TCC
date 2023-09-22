def insere(lista_numero,n):
    '''Funcao que acrescenta um numero n numa lista crescente mantendo sua ordenacao;
    list,int -> list'''
    lista_numero.insert(0,n)
    return sorted(lista_numero)