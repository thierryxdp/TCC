def filtraMultiplos(lista, numero):
    '''Função que recebe uma lista com numeros e um numero isolado e retorna 
    outra lista contendo os elementos da lista original que forem divisiveis
    por esse numero
    lista, int -> lista'''
    i=0
    resultado = []
    numero = lista[i]
    while lista[i]%numero == 0:
        resultado.append(lista)
        i += 1
        return resultado