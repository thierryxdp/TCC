def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um numero, filtra a lista pelos múltiplos deste numero para uma nova lista e a retornar, mostrando os numeros diviseis.
list,int -> list'''
    i = 0
    nova_lista = []
    while i < len(lista):
        if lista[i] % n == 0:
            nova_lista.append(lista[i])
        i = i + 1
    return nova_lista