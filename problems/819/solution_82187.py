def filtraMultiplos(lista, numero):
    '''Função que recebe uma lista com numeros e um numero isolado e retorna 
    outra lista contendo os elementos da lista original que forem divisiveis
    por esse numero
    lista, int -> lista'''
    resultado = []
    i=0
    while i < len(lista):
        numero = lista[i]
        resultado.append(numero)
        i += 1
        return resultado