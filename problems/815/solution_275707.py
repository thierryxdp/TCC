def insere(lista_numero,n):
    """Função que acrescenta um número n numa lista crescente mantendo sua ordenação.
    Use lista_numero: lista crescente.
    Use n: valor referente ao número que será inserido.
    list,int -> list"""
    lista_numero.insert(0,n)
    return sorted(lista_numero)