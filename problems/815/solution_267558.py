def  insere(lista_numero,n):
    "Função que acrescenta um número na lista crescente manter sua ordenação."
    lista_numero.insert(0,n)
    return  sorted(lista_numero)