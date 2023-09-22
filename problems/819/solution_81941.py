def filtraMultiplos (lista_de_numeros, numero):
    '''Função que dada uma lista de números e um número
    filtra aqueles que são múltiplos desse número.'''
    #list, int -> int
    seguinte = 1
    lista_de_multiplos = []
    while seguinte < len(lista_de_numeros):
        if seguinte % numero == 0:
            lista_de_multiplos = [seguinte]
        seguinte = seguinte + 1
    return lista_de_multiplos