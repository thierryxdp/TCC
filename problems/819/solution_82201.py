def filtraMultiplos(lista, numero):
    '''Função que recebe uma lista com numeros e um numero isolado e retorna 
    outra lista contendo os elementos da lista original que forem divisiveis
    por esse numero
    lista, int -> lista'''
    i=0
    resultado = [lista[]]
    numero = lista[i]
    while i < len(lista):
        if lista[i]%numero == 0:
            resultado.append(numero)
            i += 1
            return resultado