def repetidos (lista_igual) :
    """Funcao que recebe uma lista de numeros e retorna o numero de vezes que um elemento desta lista e igual ao elemento anterior"""
    contador = 0
    x = 1
    while x < len(lista_igual):
        if lista_igual[x] == (lista_igual[x-1]):
            lista_igual.count(lista_igual[x])
            contador += 1
        x += 1
    return contador